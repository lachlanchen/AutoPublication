# Integrated hosted service and owner Pi endpoint

The current service is **https://edit.lazying.art**. Invited users enter at
**https://edit.lazying.art/accounts**. A separate domain is optional, not
required for the trusted invite pilot. The original owner's credentials and
private Pi remain unchanged: its backend is a special existing publication
endpoint alongside the new Docker endpoints, not a shared worker for guests.

This repository pins the implementation; it does not copy private deployment
state. Read the authoritative LazyEdit guides:

- [Docker setup and resource/storage limits](https://github.com/lachlanchen/LazyEdit/blob/ade9de4/references/2026-10-03-hosted-multiuser-docker.md)
- [Current LazyEdge routing and rollback](https://github.com/lachlanchen/LazyEdit/blob/ade9de4/references/2026-10-03-edit-lazyedge-hosted-deployment.md)
- [Existing owner operations](https://github.com/lachlanchen/LazyEdit/blob/ade9de4/references/studio/operations.md)

## Service boundaries

```text
Current Caddy/TLS + LazyEdge + reverse SSH
  └─ authenticated Studio ingress
       ├─ existing owner → existing LazyEdit → owner-only Pi AutoPublish
       └─ invited account → own Docker workspace
                               ├─ Studio + LazyEdit + AutoPublish + desktop
                               ├─ own media/settings/profiles/queue volume
                               └─ own PostgreSQL database
```

Media stays local. HuanaYun is a small streaming ingress, not a media store,
render worker or browser host. Containers share image layers, not writable
account state. Each workspace serializes its own publications. Existing-owner
tasks continue through the original queue. No live endpoint is restarted by
checking out or updating these pinned sources.

Only the private provisioner can access Docker. The public gateway has no
Docker socket or caller-controlled image/mount/command fields. An expired
invited session fails closed rather than falling through to the owner. Raw
VNC/CDP/database/backend ports stay private. The user's desktop requires their
browser session plus an exact Origin check through the authenticated edge.

## Starting a new installation

Use Linux x86-64, Docker Engine/Compose, Node 22 and a Python environment with
the client dependencies. The initial container uses portable CPU Whisper; GPU
scheduling and ARM builds are separate work. Initialize source submodules:

```bash
git submodule update --init --recursive
scripts/autopublication build
scripts/autopublication --state "$HOME/.local/share/autopublication-new" init studio.example.com
```

Configure provider keys privately using `LazyEdit/deploy/hosted/providers.env.example`,
then start that state and deliver invitations privately. Independent-domain
mode requires domain/workspace DNS and certificates. Same-host mode uses
`init DOMAIN --same-host` plus the reviewed Studio/LazyEdge ingress adapter;
initialization alone does not edit DNS/Caddy or deploy a public route.
Do not run a bootstrap/firewall recipe against existing shared ingress.

## Operating the existing installation

```bash
scripts/autopublication status
scripts/autopublication invite
```

The default private state is `~/.local/share/lazyedit-hosted`. Invitations are
single-use and expire after 72 hours. Existing-owner login is at the usual URL;
guests register/login at `/accounts` and open their Studio to upload, correct,
process and preview. Social accounts are not required. Publication and
**Platform accounts** are optional operator-enabled capabilities; ordinary
members and the reviewer cannot open those desktops or submit posts.
Do not put owner SMTP recipients, cookies or profiles in the template. Use
separate provider credentials/budgets before wider invitations.

The original owner API base is `https://edit.lazying.art`. Each guest's
`GET /accounts/account` reports an `apiBase` such as
`https://edit.lazying.art/workspaces/<id>`. Other tools must use that base for
all scoped token/login/refresh/upload/process/publish calls. The integration
wrapper requires an explicit `--server` to avoid an accidental owner endpoint.

```bash
scripts/autopublication client \
  --server 'https://edit.lazying.art/workspaces/<id>' \
  --state /private/client-session.json \
  login --account-file /private/account.json
```

Normal processing uses corrected subtitles and contextual correction prompts.
Treat scripts/lyrics/background as references; preserve the actual speech,
timing and intended meaning. Inspect apparent omissions or abnormal lines.
Metadata describes the video/song, not internal production or prompt details.
Reuse finished runs/packages when adding platforms; never regenerate or blindly
republish an already submitted post. Publication keeps existing explicit review
and idempotency rules. Music is a separate queued task with corrected lyrics,
cover and all supported fields. The wrapper doesn't bypass those contracts.

## Storage, updates and private information

One canonical user media store is shared by editing and publication. Uploads
are renamed into the library; the publisher references the existing local ZIP.
Per-job extraction scratch is removed after terminal jobs. Source, processed
master and ZIP are distinct required artifacts; no arbitrary deletion of media
or correction history occurs. Never use `docker compose down -v` as an upgrade.

Commit/push owning-module fixes first, then bump root pins. Test before
promoting immutable releases and retain exact previous units/config for
rollback. Preserve the owner Pi/backend and other shared gateway sites. The
owner-only promotion helpers now refuse to remove the hosted router.

Passwords, API keys, tokens, browser profiles, cookies, private databases and
media must not be staged. They stay in local private state or the operator's
Nutstore Share/LazyEdit folder. `scripts/check_public_files.py` checks the index;
also inspect the diff and audit owning modules separately. Gitignore isn't a
secret remover and no scanner proves that every kind of sensitive prose is safe.

## Verified scope

Public account registration, provisioning, owner login/library, private desktop
WSS/RFB, anonymous denial, scoped API login, resumable upload/SHA-256 and a single
canonical upload were verified. The full web UI rendered without page errors.
Thirty-eight hosted/Studio contracts and three focused Python promotion checks
pass. Live member/admin permissions, asset isolation, forged headers and PWA
editing/preview were verified. No real social post was used as a smoke test.
Only publication-enabled accounts need their own platform authentication.

The source test suite includes React error-rendering checks. Install the locked
frontend dependencies with `npm ci --prefix LazyEdit/app --no-audit --no-fund`
before `scripts/autopublication test`. On a shared workstation, an existing
installation of these exact dependencies may be reused through `NODE_PATH`.

This is an invite-only pilot, not an untrusted public hosting claim. Shared
browser origin, container Chromium's current sandbox mode, storage quotas,
account recovery and global GPU scheduling require further work before
open registration. A separate domain/subdomain deployment can provide stronger
browser-origin separation while retaining the same owner/Pi endpoint design.

## Native apps, mobile login and account lifecycle

The iOS, Android and Mac Catalyst interfaces provide native library, upload,
publication settings, activity and account screens. The existing editor and
private platform login desktop remain available through authenticated web
views. Eleven UI languages are included. Only `lachlanchen` can select the
original Pi; members receive their own Docker workspace and the authorized
Vancouver sample, with no access to the owner's library or profiles.

The desktop uses one bounded viewer per workspace. Zoom and a frozen QR image
reuse that desktop; freezing disconnects streaming. Closing a selected browser
preserves its profile, leaves a blank restricted desktop and refuses closure
while publishing. Managed browser allowlists and shortcut restrictions retain
publisher CDP uploads while preventing general desktop/file-browser use.
These restrictions never modify the owner Pi.

Members can delete their account after password confirmation, provided both
queues and manual processing are idle. Grants are revoked immediately, then
the provisioner removes only that member's confirmed volumes. Capacity is
released after cleanup. Existing social posts remain on their platforms.

Google linking, fresh sign-in and real provider revocation passed in the own
identity-only External/Testing project. Apple primary/Services ID/key setup is
complete; actual authentication/revocation is unqualified. Credentials remain
private. Gateway, provisioner and the two permanent workers now run immutable
`editor-first-20261004h` images from LazyEdit source `9fbe02b`. Volumes, original
backend, Pi, shared ingress and LazyTunnel were preserved.

USD 0.99 download pricing is configured on both stores. Approved monthly
prices are 2.99/14.99/29.90 with conservative 10/60/150 source-video minutes
per UTC month. Hosted pilot limits are enforced; finished-run reuse needs no
new processing allowance. Apple draft USA prices and eleven benefit locales
were saved/read back. Google product names and benefits are drafts with no
active base plans. Real purchase/restore/refund tests and paid-download credit
remain pending, so billing stays disabled. See the pinned
[identity operations](../LazyEdit/references/studio/identity-operations.md) and
[release follow-through](../LazyEdit/references/studio/2026-10-04-release-follow-through.md).

Public review remains separate from test distribution. The reviewer has the
same editing-only capabilities as ordinary members and does not need social
credentials. Store text discloses operator-enabled publication; do not certify
access to all publishing features from editing QA alone. The owner's Pi,
channels, media and login sessions are never supplied to review.

## Optional managed publication

The private configuration uses `publishing.enabled`,
`publishing.administrators` and immutable `publishing.accountIds`. Missing policy
fails closed. Invitations, subscriptions, client headers and OAuth login do not
grant publishing. Gateway and worker enforce this on every request, including
old broad device grants. Disabled accounts can prepare/preview without dispatch;
video/music posts and platform desktop access are rejected before job creation.
Global disable pauses hosted publication. The original personal endpoint keeps
its existing behavior and owner-only routing.

Linked apps must inspect authenticated `capabilities.publishing` and granted
scopes. Use [the capability handoff](../LazyEdit/references/studio/editor-first-and-optional-publication.md)
for configuration, review access and API behavior. No account-specific runtime
configuration belongs in Git.

Read the pinned [account and release handoff](../LazyEdit/references/2026-10-04-hosted-account-and-release-handoff.md)
for the private-cell promotion, idle checks, rollback and qualification steps.
TestFlight/internal availability and public review are separate states; the
exact native release facts belong in the pinned source's `store/studio/release.json`.
