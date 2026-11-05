# IP Multimedia Subsystem (IMS)

## Evolution
- Core network evolved from three-in-one (control + bearer + service) to separated control/bearer/service → unified session control center, subscriber data center, media resource center.
- Architecture path: analog switch → digital SPC (Stored Program Control) switch → R4 softswitch → IMS.

## Definition (3GPP TS 23.002)
- **IMS** = **IP Multimedia Subsystem**: all CN (Core Network) elements for IP multimedia services (audio, video, text, chat, combos) over the PS domain.
- Entities: CSCF, MGCF, MRF, etc. (TS 23.228 Stage 2; TS 22.228 service examples).
- **IP** = IP-based transmission, session control, service implementation.
- **Multimedia** = multiple media (voice, video, image, text); terminals of different capabilities via multiple access modes.
- **Subsystem** = reuses existing network tech/equipment to the maximum.

## Further Understanding
- Multimedia AS, SIP AS, border control (IBCF = Interconnection Border Control Function), call admission (UAAF/CLF/P-CSCF), call control (CSCF), media path (BGF = Border Gateway Function), telephony AS, HSS/UPS, MRF (media server), MGCF/MGW/SGW.

## IMS Network Architecture (layers)
- **OSS/BSS**: OCS, FNR (NPDB), MAP, iCG, CCF, Rf/Ro, ATS, MMTel AS, Centrex AS, ISC (SIP), SPG, 3rd-party AS, EMM/EMA, U2020, EMS, ENS VMS, ENUM/DNS, SE, CSC, MGCF, MRFP, HSS, IM-MGW, UAC, AGCF, A-SBC/P-CSCF.
- **Access**: AG/IAD, SIP, MSAN, TDM, PBX.
- **Terminal**: SIP soft phone, BRA, POTS, mobile.

## Registration & Call Flow
- Location update/registration scenarios: attach/initial, normal/forced, periodic, combined, de-registration.
- Home/visited network flows: UE registers; P-CSCF in visited domain routes to home; S-CSCF processes auth; HSS provides auth data; call invite flows.

## IMS Service Concept
- **VAS** = Value-Added Services: premium features/add-ons to basic core (voice/data); can stand alone (SMS, USSD); stimulate demand.
- Terms:
  - Mobile operator, **OTT** (Over-The-Top apps over carrier infra), service, channel.
  - **MO** = Mobile Originated; **MT** = Mobile Terminated.
  - **AO** = Application Originated; **AT** = Application Terminated.
  - **USSD**, **MAP** (Mobile Application Part), **Diameter** (charging), **BSS** (Business Support System — billing/provisioning), **ESME** (External Short Messaging Entity for A2P).

## SMS Traffic Types
- **P2P** (Person-to-Person): traditional SMS via SMSC; HLR lookup; store & forward.
- **A2P** (Application-to-Person): automated business messages (alerts, 2FA, marketing) via aggregators, branded sender IDs, TPS.
- **P2A** (Person-to-Application): user sends to short code → application.
- **A2A** (Application-to-Application): M2M (smart meters, manufacturing, tracking, security, healthcare).

## USSD
- Real-time session-based protocol, codes *...#; USSD gateway routes to external servers (HTTP/SOAP); interactive XML menus; PULL/PUSH; no data connection needed.

## SIM OTA (SIM Over-The-Air)
- Remote SIM management: PLMN/roaming updates, SPN change, keys, applets, SMSC. Secure bridge operator↔SIM.

## SIP (Session Initiation Protocol)
- Functions: user location, capabilities, availability, call setup, call control.
- Features: simple text (like HTTP/SMTP), extensible (SDP/MSML), flexible (vendor headers).
- Transaction: INVITE → 183 → 180 → 200 → ACK; BYE → 200. Basic call flow with proxies.

## Diameter
- Main function in IMS: registration/authentication/session setup/charging (quiz).
- Requests/answers: ASR/ASA, ACR/ACA, CER/CEA, DWR/DWA, DPR/DPA, RAR/RAA, STR/STA.
- Cx application messages: UAR/UAA, SAR/SAA, LIR/LIA, MAR/MAA, RTR/RTA, PPR/PPA (codes 300–305).

## UE Voice Domain Preference
- Four domain preferences: CS Only, IMS Only, CS Preferred/IMS Second, IMS Preferred/CS Second.
- UE usage: voice, data.

## Thank you.
