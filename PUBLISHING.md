# Creating the GitHub repository privately

Create the remote as **Private** first. The local repository is already named
`algorithm-frontier` and has a `main` branch.

## With GitHub CLI

After installing `gh` and signing in:

```bash
gh auth login
gh repo create algorithm-frontier --private --source . --remote origin --push
```

Run that command from this repository directory. It creates the private remote,
adds `origin`, and pushes the current commits. Later batches use:

```bash
git add .
git commit -m "Curate <problem area>"
git push
```

## With the GitHub website

1. On GitHub choose **New repository**.
2. Set the name to `algorithm-frontier`, choose **Private**, and do not add a
   README, license, or `.gitignore` because they already exist locally.
3. Copy the SSH or HTTPS remote URL and run:

```bash
git remote add origin <REMOTE-URL>
git push -u origin main
```

Keep the repository private while the remaining modules are being curated.
Before making it public, review the source-license boundaries, remove or mark
superseded material according to `MAINTENANCE.md`, and check that every public
claim has a proof and verify set.
