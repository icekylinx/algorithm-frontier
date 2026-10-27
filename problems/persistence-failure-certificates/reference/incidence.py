"""Exact general incidence failure summaries, including top-cell labels.

Copyright 2026 Yilin Liu. Authored by GPT-6 Astra Pro. Apache-2.0.
This implementation generates actual independent feature rows per original
row and merges them, avoiding enumeration of a potentially huge monomial set.
"""
from math import comb
from feature_summary import (Field, Echelon, _order, _label_points,
    _multiply_linear, independent_row_indices, evaluation_module, boundary_matrix)


def incidence_summary(rows, row_labels, column_labels, failures, modulus=None, order=None):
    """Retain original columns preserving every allowed surviving prefix span.

    Label IDs are sortable integers. Modulus is a caller-supplied prime;
    the explicit field must contain enough distinct nonzero label points.
    Complete original matrix input is charged separately from retained output.
    """
    rows=tuple(tuple(r) for r in rows)
    row_labels=tuple(frozenset(r) for r in row_labels)
    column_labels=tuple(frozenset(c) for c in column_labels)
    n=len(column_labels)
    if type(failures) is not int or failures<0 or len(rows)!=len(row_labels):
        raise ValueError('nonnegative integral budget and one label set per row required')
    if any(len(r)!=n for r in rows):raise ValueError('matrix width must equal column-label count')
    if any(type(x) is not int for s in row_labels+column_labels for x in s):
        raise ValueError('integer original label IDs required')
    f=Field(modulus)
    ids=_order(n,order)
    matrix=[[f.value(r[e]) for e in ids] for r in rows]
    labels=row_labels+column_labels
    points=_label_points(labels,f)
    failures=min(failures,len(points))
    increment=0
    for i,r in enumerate(rows):
        for e,x in enumerate(r):
            if f.value(x):
                if not row_labels[i]<=column_labels[e]:
                    raise ValueError('nonzero incidence violates label containment')
                increment=max(increment,len(column_labels[e]-row_labels[i]))
    selected=independent_row_indices(matrix,f)
    global_rows=Echelon(n,f)
    candidates=0
    for i in selected:
        coords=[[f.zero]*n for _ in range(increment)]
        for j,e in enumerate(ids):
            if not matrix[i][j]:continue
            polynomial=[f.one]
            for label in sorted(column_labels[e]-row_labels[i]):
                polynomial=_multiply_linear(polynomial,f.one,f.sub(f.zero,f.inv(points[label])),f)
            for a,x in enumerate(polynomial[1:]):coords[a][j]=x
        module=evaluation_module([matrix[i]],coords,failures,f)
        candidates+=module.candidates
        for row in module.vectors:global_rows.insert(row)
    return {'retained':tuple(ids[j] for j in global_rows.pivots),
            'rank':global_rows.rank,'original_rank':len(selected),
            'selected_original_rows':selected,'increment':increment,
            'formal_rows':len(selected)*comb(failures+increment,increment),
            'candidates':candidates}


def labeled_persistence_summary(vertices,top_simplices,vertex_labels,top_labels,
                                failures,modulus=None,order=None):
    """Preserve lower homology with vertex labels and additional top labels.

    The full original lower skeleton is implicitly retained. One original
    top-simplex order is supplied; no arbitrary independent order is combined.
    """
    if type(vertices) is not int or vertices<0 or len(vertex_labels)!=vertices:
        raise ValueError('one label set per original vertex required')
    simplices=tuple(tuple(s) for s in top_simplices)
    if len(top_labels)!=len(simplices):raise ValueError('one additional label set per top simplex required')
    vertices_labels=tuple(frozenset(x) for x in vertex_labels)
    top_labels=tuple(frozenset(x) for x in top_labels)
    if any(type(x) is not int for labels in vertices_labels+top_labels for x in labels):
        raise ValueError('integer original label IDs required')
    faces,rows=boundary_matrix(vertices,simplices,Field(modulus))
    row_labels=[set().union(*(vertices_labels[v] for v in face)) for face in faces]
    columns=[set(top_labels[e]).union(*(vertices_labels[v] for v in simplex)) for e,simplex in enumerate(simplices)]
    result=incidence_summary(rows,row_labels,columns,failures,modulus,order)
    result['faces']=tuple(faces)
    return result
