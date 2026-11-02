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
its supported integration in Codex. The requested mode is on-demand dispatch:
when a task is assigned, select its specialist automatically using `AGENTS.md`.
The user need not name an agent or provide a fixed content task during setup.
Use the assigned task as input and the configured client workspace as context.
No job or external event handler is active merely because this file exists.

For the current cloud environment, the configured private client workspace is
recorded in the saved startup instructions. Keep that account context local.

Use this dispatcher instruction when the actual scheduler supports registering
an on-demand handler:

```text
Open the existing repository checkout and read AGENTS.md.
Assigned task: <incoming task payload>
Client workspace: <configured private client directory>
Select and read the appropriate skill automatically using the task-routing table.
For multi-stage work, use social-media-manager-codex to coordinate specialists.
Execute the assigned task within its authorized scope and record its result or
concrete blocker in the client's workflow status. If no task payload is present,
remain idle; do not invent a task or recurrence.
```

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

Recurring runs are optional and require a separately specified deliverable and
cadence. Use `Asia/Kolkata` as the default time zone unless the user specifies
otherwise. Keep credentials in the destination's secure settings. A social
publishing provider such as Blotato is a separate integration; none was installed
or authenticated here.
