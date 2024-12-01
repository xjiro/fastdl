# Github Pages for GoldSrc FastDL

This is an forkable fastdl directory for goldsrc games that will will use github pages for hosting.


## Usage

1. **Fork this repository** to your GitHub account.

2. **Activate Github Pages** in the repo settings.

3. **Configure your game server** `sv_downloadurl https://<username>.github.io/fastdl/moddir/`

4. **(Optional) Generate the index** Run `python generate.py` and commit the new index.html.


## Limitations

1. Free Github repos are limited to 1GB in size. If you've ever removed files, you can better utilize this space by deleting git history:

```sh
git checkout --orphan new-initial-branch
git add -A
git commit -m "reset history"
git branch -D master
git branch -m master
git push --force origin master
```

2. Free Github repos are limited to 100GB of bandwidth per month.

## License

This project is licensed under the MIT License.
