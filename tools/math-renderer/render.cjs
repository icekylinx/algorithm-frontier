#!/usr/bin/env node
'use strict';
// Produce standalone SVGs with local glyph paths, no fonts, scripts or URLs.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const [requestPath, outputPath] = process.argv.slice(2);
if (!requestPath || !outputPath) throw Error('usage: render.cjs REQUEST_JSON OUTPUT_DIRECTORY');
const requests = JSON.parse(fs.readFileSync(requestPath, 'utf8'));
const xml = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  // Preserve source whitespace exactly without serializing line-end blanks.
  .replace(/[ \t]+(?=\r?\n)/g, blanks => blanks.replace(/ /g, '&#32;').replace(/\t/g, '&#9;'));
function standaloneTag(source) {
  // MathJax normally positions manual equation tags in a responsive 100%-wide
  // outer SVG without a viewBox. A repository image needs a fixed canvas.
  // Keep the exact source in its title and place the same visible label after
  // the formula, so both are included in one ordinary mathematical viewBox.
  const match = /\\tag(\*)?\s*\{/.exec(source);
  if (!match) return source;
  let end = match.index + match[0].length, depth = 1;
  const start = end;
  while (end < source.length && depth) {
    if (source[end] === '\\') { end += 2; continue; }
    if (source[end] === '{') depth++;
    if (source[end] === '}') depth--;
    end++;
  }
  if (depth) throw Error('unclosed equation tag');
  const label = source.slice(start, end-1);
  const body = (source.slice(0, match.index) + source.slice(end)).trim();
  return body + '\\qquad\\text{' + (match[1] ? label : '('+label+')') + '}';
}
fs.mkdirSync(outputPath, {recursive:true});
let completed = 0;
for (const {key, tex} of requests) {
  if (crypto.createHash('sha256').update(tex).digest('hex').slice(0,24) !== key)
    throw Error('source digest mismatch: ' + key);
  const doc = mathjax.document('', {
    InputJax:new TeX({packages:AllPackages.filter(p => !['noerrors','noundefined'].includes(p)),
      formatError:(_jax,error) => {throw error;}}),
    OutputJax:new SVG({fontCache:'local'})
  });
  const outer = adaptor.outerHTML(doc.convert(standaloneTag(tex), {display:true}));
  if (outer.includes('data-mjx-error')) throw Error('MathJax error: ' + key);
  let svg = outer.slice(outer.indexOf('<svg'), outer.lastIndexOf('</svg>') + 6);
  // Each image is independent. Stable local IDs make output reproducible.
  svg = svg.replace(/MJX-\d+-/g, 'M-').replace(/\sdata-mml-node="[^"]*"/g, '')
    .replace(/\sdata-c="[^"]*"/g, '').replace(/\srole="[^"]*"/g, '')
    .replace(/\sfocusable="[^"]*"/g, '').replace(/\sstyle="[^"]*"/g, '')
    .replace(/\scurrentColor/g, ' currentColor');
  const match = /^<svg\b[^>]*\bviewBox="([^"]+)"/.exec(svg);
  if (!match) throw Error('missing viewBox: ' + key);
  const [x,y,w,h] = match[1].split(/\s+/).map(Number);
  const padding = 180;
  svg = svg.replace(/viewBox="[^"]+"/, `viewBox="${x-padding} ${y-padding} ${w+2*padding} ${h+2*padding}"`)
    .replace(/\bwidth="[^"]+"/, `width="${((w+2*padding)/1000*17).toFixed(2)}"`)
    .replace(/\bheight="[^"]+"/, `height="${((h+2*padding)/1000*17).toFixed(2)}"`)
    .replace('<svg ', '<svg role="img" aria-labelledby="title" ')
    .replace('>', `><title id="title">${xml(tex)}</title><rect x="${x-padding}" y="${y-padding}" width="${w+2*padding}" height="${h+2*padding}" fill="white"/>`)
    .replace(/currentColor/g, '#1f2328');
  fs.writeFileSync(path.join(outputPath, key+'.svg'), svg+'\n');
  completed++;
  if (completed % 500 === 0) process.stdout.write(`Rendered ${completed}/${requests.length} equations\n`);
}
process.stdout.write(`Rendered ${completed} standalone equations\n`);
