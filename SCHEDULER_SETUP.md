# Scheduler handoff

The uploaded pack has no scheduler service, API client, or recurring-task
registration. `publisher-codex` prepares publishing plans; it does not run them
on a timer. No external scheduler was connected during this installation.

## Run on demand in Codex

Open this repository in a new Codex session after running `bash install.sh`.
For a client workspace, use:

```text
Use social-media-manager-codex for clients/<client>.
Inspect its current workflow status, run the next requested stage, and save
outputs under that client directory. Report anything blocked by missing inputs.
```

For a publishing handoff, use `publisher-codex` with the approved client files.

## Connect a task scheduler

To register the agent in Codex Scheduler, supply the actual service URL or enable
its supported integration in Codex. Registration also needs a client workspace,
the task to run, and either an on-demand trigger or a recurrence and time zone.
Use `Asia/Kolkata` as the default time zone unless the user specifies otherwise.
No recurring job is active merely because this file exists.

The scheduler must open this repository, load the requested skill, and use an
authenticated Codex runtime. Install Python dependencies from
`requirements-motion.txt` if the task includes motion export. Live processes
must be restarted by the scheduler; an environment snapshot retains files only.

Suggested task body for a draft-only recurring run:

```text
In this repository, read skills/social-media-manager-codex/SKILL.md.
Work only in clients/<client>. Inspect context/workflow-status.md and produce
the requested draft deliverable. Record completed and blocked work in that
status file. Do not publish posts or submit social-platform schedules.
```

Choose the client, deliverable, recurrence, and time zone before registering a
recurring task. Keep credentials in the destination's secure settings. A social
publishing provider such as Blotato is a separate integration; none was installed
or authenticated here.
