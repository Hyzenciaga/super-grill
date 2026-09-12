# Shopping list spec

R1: Adding an item works with the device disconnected from every network.
Architecture: Adding an item waits for a successful HTTP POST before it appears.

R2: A user can undo marking an item bought and recover its original name/quantity.
Storage: Marking bought immediately deletes the item and all item data; there is no archive or undo buffer.
