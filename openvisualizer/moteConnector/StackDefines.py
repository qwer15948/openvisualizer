# DO NOT EDIT DIRECTLY!
# This file was generated automatically by GenStackDefines.py
# on Fri, 08 Mar 2019 20:58:25
#

components = {
   0: "NULL",
   1: "OPENWSN",
   2: "IDMANAGER",
   3: "OPENQUEUE",
   4: "OPENSERIAL",
   5: "PACKETFUNCTIONS",
   6: "RANDOM",
   7: "RADIO",
   8: "IEEE802154",
   9: "IEEE802154E",
  10: "SIXTOP_TO_IEEE802154E",
  11: "IEEE802154E_TO_SIXTOP",
  12: "SIXTOP",
  13: "NEIGHBORS",
  14: "SCHEDULE",
  15: "SIXTOP_RES",
  16: "OPENBRIDGE",
  17: "IPHC",
  18: "FORWARDING",
  19: "ICMPv6",
  20: "ICMPv6ECHO",
  21: "ICMPv6ROUTER",
  22: "ICMPv6RPL",
  23: "OPENUDP",
  24: "OPENCOAP",
  25: "C6T",
  26: "CEXAMPLE",
  27: "CINFO",
  28: "CLEDS",
  29: "CSENSORS",
  30: "CSTORM",
  31: "CWELLKNOWN",
  32: "UECHO",
  33: "UINJECT",
  34: "RRT",
  35: "SECURITY",
  36: "USERIALBRIDGE",
  37: "UEXPIRATION",
  38: "UMONITOR",
  39: "CJOIN",
  40: "OPENOSCOAP",
  41: "CINFRARED",
  42: "CLICKER",
}

errorDescriptions = {
   1: "received an echo request",
   2: "received an echo reply",
   3: "getData asks for too few bytes, maxNumBytes={0}, fill level={1}",
   4: "the input buffer has overflown",
   5: "the command is not allowed, command = {0}",
   6: "unknown transport protocol {0} (code location {1})",
   7: "wrong TCP state {0} (code location {1})",
   8: "TCP reset while in state {0} (code location {1})",
   9: "unsupported port number {0} (code location {1})",
  10: "unexpected DAO (code location {0}). A change maybe happened on dagroot node.",
  11: "unsupported ICMPv6 type {0} (code location {1})",
  12: "unsupported 6LoWPAN parameter {1} at location {0}",
  13: "no next hop for layer 3 destination {0:x}{1:x}",
  14: "invalid parameter",
  15: "invalid forward mode",
  16: "large DAGrank {0}, set to {1}",
  17: "packet discarded hop limit reached",
  18: "loop detected due to previous rank {0} lower than current node rank {1}",
  19: "upstream packet set to be downstream, possible loop.",
  20: "packet received from mote {0:x}{1:x} is dropped",
  21: "neighbors table is full (max number of neighbor is {0})",
  22: "there is no sent packet in queue",
  23: "there is no received packet in queue",
  24: "schedule overflown",
  25: "wrong celltype {0} at slotOffset {1}",
  26: "unsupported IEEE802.15.4 parameter {1} at location {0}",
  27: "got desynchronized at slotOffset {0}",
  28: "synchronized at slotOffset {0}",
  29: "large timeCorr.: {0} ticks (code loc. {1})",
  30: "wrong state {0} in end of frame+sync",
  31: "wrong state {0} in startSlot, at slotOffset {1}",
  32: "wrong state {0} in timer fires, at slotOffset {1}",
  33: "wrong state {0} in start of frame, at slotOffset {1}",
  34: "wrong state {0} in end of frame, at slotOffset {1}",
  35: "maxTxDataPrepare overflows while at state {0} in slotOffset {1}",
  36: "maxRxAckPrepapare overflows while at state {0} in slotOffset {1}",
  37: "maxRxDataPrepapre overflows while at state {0} in slotOffset {1}",
  38: "maxTxAckPrepapre overflows while at state {0} in slotOffset {1}",
  39: "wdDataDuration overflows while at state {0} in slotOffset {1}",
  40: "wdRadio overflows while at state {0} in slotOffset {1}",
  41: "wdRadioTx overflows while at state {0} in slotOffset {1}",
  42: "wdAckDuration overflows while at state {0} in slotOffset {1}",
  43: "busy sending",
  44: "sendDone for packet I didn't send",
  45: "no free packet buffer (code location {0})",
  46: "freeing unused memory",
  47: "freeing memory unsupported memory",
  48: "unsupported command {0}",
  49: "unknown message type {0}",
  50: "wrong address type {0} (code location {1})",
  51: "bridge mismatch (code location {0})",
  52: "header too long, length {1} (code location {0})",
  53: "input length problem, length={0}",
  54: "booted",
  55: "invalid serial frame",
  56: "invalid packet frome radio, length {1} (code location {0})",
  57: "busy receiving when stop of serial activity, buffer input length {1} (code location {0})",
  58: "wrong CRC in input Buffer",
  59: "synchronized when received a packet",
  60: "security error on frameType {0}, code location {1}",
  61: "sixtop return code {0} at sixtop state {1}",
  62: "there are {0} cells to request mote",
  63: "the cells reserved to request mote contains slot {0} and slot {1}",
  64: "the slot {0} to be added is already in schedule",
  65: "the received packet format is not supported (code location {0})",
  66: "the metadata type is not suppored",
  67: "the received packet has expired",
  68: "packet expiry time reached, dropped",
  69: "node joined",
  70: "OSCOAP sequence number reached maximum value",
  71: "OSCOAP buffer overflow detected (code location {0})",
  72: "OSCOAP replay protection failed",
  73: "OSCOAP decryption and tag verification failed",
  74: "Aborted join process (code location {0})",
}

sixtop_returncode = {
   0: "RC_SUCCESS",
   1: "RC_EOL",
   2: "RC_ERROR",
   3: "RC_RESET",
   4: "RC_VER_ERR",
   5: "RC_SFID_ERR",
   6: "RC_SEQNUM_ERR",
   7: "RC_CELLLIST_ERR",
   8: "RC_BUSY",
   9: "RC_LOCKED",
}

sixtop_statemachine = {
   0: "IDLE",
   1: "WAIT_ADDREQUEST_SENDDONE",
   2: "WAIT_DELETEREQUEST_SENDDONE",
   3: "WAIT_RELOCATEREQUEST_SENDDONE",
   4: "WAIT_COUNTREQUEST_SENDDONE",
   5: "WAIT_LISTREQUEST_SENDDONE",
   6: "WAIT_CLEARREQUEST_SENDDONE",
   7: "WAIT_ADDRESPONSE",
   8: "WAIT_DELETERESPONSE",
   9: "WAIT_RELOCATERESPONSE",
  10: "WAIT_COUNTRESPONSE",
  11: "WAIT_LISTRESPONSE",
  12: "WAIT_CLEARRESPONSE",
}
