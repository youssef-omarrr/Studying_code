# IMS Signaling System — Part 1: IMS Architecture

## Why learn IMS
- LTE growing; VoLTE (Voice over LTE) services provided by IMS; IMS knowledge necessary.

## Scope & Objectives
- Scope: IMS Architecture (nodes, specs, protocols), mobile access to IMS, VoLTE concepts.
- Objectives: describe architecture (logical nodes, specs, protocols); explain mobile access & VoLTE.

## Overview
- IMS Standardization, Architecture (nodes/functions), Registration & Authentication, Mobile IMS, VoLTE Architecture & QoS.

## Specification Bodies
- **IETF**: SIP (RFC3261), SDP (RFC2327), Diameter (RFC3588), RTP (RFC3550).
- **3GPP**: TS 23.218 (IM session handling), TS 23.228 (IMS Stage 2), TS 24.228 (signaling flows).
- **ETSI/TISPAN**: wireline networks services/architecture.
- **ITU-T**: H.248 (media gateway control).
- **OMA**: instant messaging, presence, MMS.
- **IANA**: domain names, IP addresses.
- **GSMA**: VoLTE, RCS; PRDs (IR.92/94/58, IR.64/65/88 for roaming/interconnect/ICS).

## IMS definition
- All-IP network architecture for operators offering end-user services.

## Nodes & Functions
### Access (UE = User Equipment)
- PC client, SIP phone, POTS with SIP IAD, SIP ALG, 2G/3G/4G mobile with SIP client.
- POTS = Plain Old Telephone Service; IAD = Integrated Access Device; ALG = Application Layer Gateway.

### CSCF = Call Session Control Function
- **P-CSCF** (Proxy): first contact point; stateful proxy; tracks registrations & active sessions; stores UE contact (IP/port); enforces min/max registration times; forwards SIP between access and home network.
- **I-CSCF** (Interrogating): entry point for connections terminating in home IMS; assigns S-CSCF during initial registration with HSS; routes SIP from other networks to S-CSCF.
- **S-CSCF** (Serving): session control — registration & auth, download user profile, trigger AS, SIP routing, number normalization, ENUM DNS query, breakout, supervision, accounting.
- **E-CSCF**: Emergency Call Session Control Function.

### HSS = Home Subscriber Server
- Master database of user/subscriber info: identification, authentication/authorization, tracks which S-CSCF user registered to, service info (triggers, AS identities). SLF for HSS discovery.

### ENUM DNS = Electronic Numbering / Domain Name System
- ENUM: phone number → SIP address. DNS: FQDN → IP. DHCP for IPv4/IPv6.

### Application Server (MTAS = Multimedia Telephony Application Server)
- MMTel AS provides end-user telephony services (call forwarding, value-add).

### SBG = Session Border Gateway
- Funnels sessions; security, QoS, SLA, NAT; implements ATCF. A-SBG (access↔IMS), N-SBG (external↔IMS).

### PSTN Gateway
- **MGC** = Media Gateway Controller: master to MGWs; call control signaling; session establishment/modification/termination; addressing/routing; H.248.
- **MGW** = Media Gateway: handles media payload; adapts to IP packets.

### Support systems
- WUIGM (Web UI for Group & Data Mgmt), OSS-RC (Operation Support System), EMA (Ericsson Multi Activation), EMM (Ericsson Multi Mediation).

## IMS Reference Architecture
- Main protocols:
  - Control: SIP, SDP, Diameter, H.248/Megaco, ISUP, H.323.
  - Media: RTP, MSRP.

## Registration & Authentication
- Registration: UE sends SIP REGISTER with current location + public user identity. Network checks home domain, authenticates, allows register.
- Auth methods:
  - **HTTP Digest**: challenge-response; password in HSS & UE.
  - **GIBA** (GPRS IMS Bundled Authentication): authenticated on GPRS attach; HSS gets UE IP, MSISDN, IMSI.
  - **NBA** (NASS Bundled Authentication): on IP access; lineID provisioned in HSS.
  - **IMS-AKA** (IMS Authentication and Key Agreement): IPSec associations UE↔P-CSCF.
- Flow: REGISTER → 401 Unauthorized (nonce) → REGISTER (response) → 200 OK.

## Mobile IMS Access
- **ISIM**: private/public ID, home domain URI, long-term secret.
- Access security: Early IMS — SIM/USIM, GIBA; Full — IMS AKA, needs USIM/ISIM.
- P-CSCF location: now home network (with GGSN/PDN-GW); future visited network.
- P-CSCF discovery: provisioned in UA or supplied by GGSN (list/DHCP).
- Registration steps: 1 bearer-level (GPRS), 2 PDP context activation, 3 CSCF discovery, 4 application-level registration.

## VoLTE Architecture
- MME = Mobility Management Entity; SGW = Serving Gateway; PGW = Packet Data Network Gateway; PCRF = Policy and Charging Rules Function.
- EPS bearer service architecture, QCI mapping, EPS bearer establishment. IP session & EPS bearers.

## Summary
- Standards orgs, nodes, registration/auth, mobile IMS, VoLTE.

## More info
- Other e-learnings: SIP in IMS, Diameter in IMS, H.248/Megaco in IMS, IMS Signaling Examples. CPI store, product catalogue. Instructor-led: MyLearning "IMS Signaling" LZU 108 7193.
