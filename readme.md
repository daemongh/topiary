Topiary - Simple python script to check for a git repo for old remote branches

## Usage

```bash
python topiary.py <path_to_repo> [<days>]
```

`<path_to_repo>` is the path to the repo
`<days>` is the number of days after the last commit in the branch before it is considered stale

## Examples

Check for stale branches in `projects/topiary` with 365 days being the stale cutoff:
```bash
python topiary.py "projects/topiary"
```

Check for stale branches in `projects/topiary` with 3 years being the stale cutoff:
```bash
python topiary.py "projects/topiary" 1095
```

Check for stale branches in `projects/topiary` and filter out the comment lines:
```bash
python topiary.py "projects/topiary" | sed /^#/d
```

## License

MIT

