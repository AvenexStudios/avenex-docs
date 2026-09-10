# Rules and penalties

## Warning
A warning announces an incident-points threshold. It does not add time or
require pit service. Each enabled incident-ladder level is issued once per
race state. A single incident crossing several thresholds selects the highest
applicable level, rather than issuing every intermediate penalty.

## Time penalty
Adds the configured seconds to the final race result. It does not require a
stop. An incident threshold of 2 points with a 3-second sanction means +3 s,
not +6 s. Track-cut throttle violations can add further seconds.

The monitor shows the accumulated total: +3 s plus two +5 s sanctions is +13 s.
Changing settings does not alter penalties already issued. Serving DT or
Stop & Go does not remove accumulated seconds.

Administrators must enable post-race processing to apply issued time to final
results. The report `cfg/avenex_post_race_results.html` shows the original time,
penalty and adjusted result. Compare total race times with equal completed
laps, not a single lap time. The latest report replaces the previous file;
archive it if you need a record.

The report is produced when race results finalize after relevant participants
finish or the race-over timeout expires. Crossing the line first does not
necessarily mean the report is ready.

## Drive-through
Serve the pit-lane obligation before the displayed lap deadline. The current
edition recognizes service while the car is in pit lane within the speed limit
plus tolerance; it does not verify a complete entry-to-exit traversal.
Missing the deadline escalates to disqualification.

## Stop & Go
Stop in pits for the duration set in Avenex enforcement. Moving above the
configured stopped-speed threshold before completion restarts the hold timer.
Completing the hold serves the penalty; missing its lap deadline escalates
to disqualification. Avenex does not teleport the car or lock its throttle.

## Disqualification
A terminal sanction. Depending on server configuration it uses native
disqualification or removes the driver from the server. It cannot be served.

## Track cuts
Four wheels outside immediately count one cut. Remaining outside does not
repeat the count; rejoining and leaving again can count another.
Lifting does not erase a cut.

After the configurable reaction margin, keep throttle at or below the maximum
for the control period. The first excess during that period immediately adds
the configured time, once per cut. Rejoining does not cancel that obligation.

At the cut limit the configured DT, Stop & Go or DSQ is issued. Cuts freeze
and pending throttle windows are cancelled; further excursions do not add
cuts or time while that limit sanction is pending. Serving its DT/Stop & Go
resets cuts to zero, not accumulated seconds. Subsequent cuts may add time again.

## Service deadlines and concurrent penalties
Lap deadlines include the current lap: do not wait until the next crossing to
begin serving. The app maintains one pending DT/Stop & Go obligation rather
than a queue of identical penalties. New settings apply to future obligations.

## Other controls
VSC/FCY is speed-limited neutralization, not a physical safety car. Manual and
automatic activation are separate options. Follow its displayed speed and
countdown when your server enables it.

Disabled blue-flag, yellow-flag or pit-speeding cards are unavailable controls;
do not rely on them enforcing a league rule. Overlay visibility is separate
from penalty enforcement.

See [Administration](server-admin.md) and [incident scoring](incidents.md).

