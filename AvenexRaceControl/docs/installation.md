# Installation

## Before you start
You need Assetto Corsa, Custom Shaders Patch (CSP) and the Avenex client package
provided by your league or Avenex administrator. Use the client and server
versions supplied together. Ask the provider for the supported CSP version;
do not assume every CSP build is compatible.

## Driver setup
1. Close the game and back up any existing Avenex configuration.
2. Extract the supplied client package into the Assetto Corsa installation,
   preserving its folder structure. The app directory is
   `apps/lua/AvenexIncidents`.
3. Enable the app through your CSP Lua-app settings and join the server.
4. Check that the expected counters and notifications are visible. If they are
   hidden, ask whether the server has disabled that overlay.
5. Re-enter the session after updating client files.

The folder name can remain AvenexIncidents even though the product name is
Avenex Race Control. Do not rename package folders manually.

## Server setup
Use an AssettoServer package compatible with the supplied Avenex plugin, not
the unmodified Assetto Corsa dedicated server executable. Keep the client,
plugin and host package versions together.

Install the plugin following the supplied package layout. Configure the admin
access token privately, then open `/avenex/admin` on the server's HTTP address.
Use [Administration](server-admin.md) to choose league rules. Do not share the
admin token with drivers or include it in public invitations.

## Updating
Back up configuration and results before replacing a package. Replace only
the files identified by its installation instructions. Existing penalties and
results are not reset merely by changing a setting. Check [versions](versions.md)
and reconnect clients after an update.

