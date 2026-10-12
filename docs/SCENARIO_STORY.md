**BEACON OF THE EAGLE LLC | CENTINELL SUITE DEFENSE**  
*Original simulated forensic case | Northbridge Systems | 26-NB-0918*

# At 01:26 UTC, the last light was still on

*18 September 2026. Night shift. Northbridge Systems (a wholly fictional company).*

A scheduled archive index rebuild was supposed to be uneventful. The backup operator confirmed a change window. The SOC saw a routine status request and closed a transient alert as noise. Then the collector stopped receiving messages from `nb-dfs-02`, the restricted-data archive node. A gateway analyst had independently noted a small outbound upload but could not determine its relationship to the approved work.

Archive-host telemetry is now partially missing. The control-plane audit and an isolated vault witness survived. The vault is not a magic source of truth: its signature secures the bytes of one witness object, while the analyst must still compare observations from independently located systems. Some services had slightly incorrect clocks. A client hostname asserted by a session cannot be trusted as a device inventory fact, and the same service account appears in legitimate and suspicious activity.

**SOC mandate:** identify the incident scope, resolve competing explanations, rebuild events with clock error bounds, distinguish data-read/staging/upload from later unknown outcomes, and preserve the chain of custody. The organization expects conclusions that can be defended in an incident review—not a guess about a famous actor.

**The twist:** the correct result is not merely *finding the missing log*. It is identifying the minimum reliable chain that survives the log loss and what that chain cannot establish.

There are no genuine clients, breached entities, victims, personal records, financial accounts or production endpoints in this case.
