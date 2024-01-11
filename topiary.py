import sys
from git import Repo
import time
import humanize
import datetime as dt

if len(sys.argv) < 2:
    print("Usage: topiary.py <directory> <age>")
    sys.exit(1)

dir = sys.argv[1]

age = 365

if len(sys.argv) > 2:
    age = int(sys.argv[2])

age_delta = dt.timedelta(days=age)
now = dt.datetime.now()
cutoff_date = now - age_delta

print(f"# Checking {dir} for stale branches older than {age} days")
repo = Repo(dir)

for ref in repo.remote().refs:
    if ref.remote_head is None:
        continue

    if (
        ref.remote_head == "master"
        or ref.remote_head == "main"
        or ref.remote_head == "HEAD"
    ):
        continue

    print(f"# Remote branch: {ref.remote_head}")
    commit = repo.rev_parse(f"origin/{ref.remote_head}")
    commit_date = dt.datetime.fromtimestamp(commit.committed_date)

    print(f"# Last commit: {commit_date} by {commit.author}")
    if cutoff_date > commit_date:
        print(
            f"# Stale branch detected - updated {humanize.naturaltime(commit_date)} ***"
        )
        print(f"git push origin --delete {ref.remote_head}")
    else:
        print(f"# Branch is up to date, moving on...")

    print("# --")
