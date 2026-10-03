# AutoPublication development and operation

- This is the integration repository. Implement fixes in the owning submodule,
  test and push there, then update the pinned gitlink here. Never copy media,
  model weights, browser profiles or credentials into this repository.
- Hosted code lives in `LazyEdit/hosted` and `LazyEdit/deploy/hosted`; it already
  contains the isolated AutoPublish worker. Root `AutoPublish` remains useful
  for standalone operation, not a second live service in hosted workspaces.
- `edit.lazying.art` serves the original owner plus invite-only workspaces.
  Preserve the original backend/Pi, account DB, profiles, queues and LazyTunnel.
  Read `docs/hosted-service.md` before changing any deployment.
- Build/test commands do not authorize a real social publication. Use synthetic
  media and no-target queue checks for verification. Never auto-retry an
  interrupted browser submission without reconciling platform history.
- Keep registration invite-only. A workspace's browser and native tokens must
  never route to the owner's Pi or another user's account. Client commands
  require an explicit API server base.
- Private state belongs outside Git, normally `~/.local/share/lazyedit-hosted`.
  No password, API key, session token, cookie, profile, account database or raw
  private evidence may be committed. Run `scripts/check_public_files.py` before
  pushing. This check is a guard, not a substitute for inspecting the diff.
- Source assets and reproducible current artifacts may be retained. Clean up
  exact disposable test containers/volumes and owned test browser processes;
  never remove a user's volume or another project's runtime.
- Keep English and all ten README translations synchronized. Commit only
  intended files; use the existing repository and preserve unrelated work.
