# Wrapper around Google Sheets API

Not clear whether this library serves a purpose or not. Basically the
Sheets API is kinda horrible with big blobs of JSON that need to be
passed around. This library takes the discovery document Google
helpfully supplies and uses it to generate an API which is
superficially quite similar to Googles own API except that it also
generates a bunch of `TypedDict` definitions so we can have the type
checker help us figure out if we're blobbing together the right blobs
of JSON.

As another (in progress) feature, there's an AST for expressing Sheets
formulas in code. More work remains to make that actually useful.
