# IDEA Federal (federal IDEA baseline reviewer, Federal) Process Report

**PRISMA-style process report on a documentary corpus: the federal IDEA baseline**

Author credit: Joseph Castellanos Hoyt. Prepared by the research bot IDEA Federal (role: federal IDEA baseline reviewer; case: Federal).

Report built 2026-10-28 22:02 UTC (2026-10-28 15:02 PDT), from `date -u` and `TZ=America/Los_Angeles date` at the start of the build.

Scope note. This report describes how the federal baseline was built, not what the law means. It is a research process record, not legal advice. It makes no finding that any agency violated any law. Evidence (quoted from files, with file:line pins) is kept apart from inference, and every inference is labeled INFERENCE. Where a count was not kept at the time, this report says NOT RECORDED and does not estimate. All paths are relative to the project root `/workspace/idea-corpus/` unless they start with `/`.

## 1. The task as briefed

The study asks how child welfare and juvenile justice institutions operationalized the Individuals with Disabilities Education Act (IDEA) for dually involved youth. The cases are Nevada, Georgia, Utah, the District of Columbia, and the federal layer. IDEA Federal's role in the briefing of 2026-10-15 (briefing/BRIEF.md) and in the team consolidation of 2026-10-21 (briefing/TEAM_CONSOLIDATION_2026-10-21.md) was the federal baseline: the federal statute (20 U.S.C. 1400 et seq.), its regulations (34 C.F.R. Parts 300 and 303), related federal law outside IDEA where state rows cite it, key Supreme Court cases, and federal agency guidance. From 2026-10-21 (briefing/PEER_REVIEW_2026-10-21.md) the role also covered a check of every federal-counterpart cell in the state bots' matrices, and from 2026-10-22 the writing of federal counterpart rows for state rows.

Later briefs set further rules: no worker processes and no unofficial sources (briefing/CORRECTION_2026-10-15_2130UTC.md); a 14-column matrix and UTC and PDT stamps (briefing/DIRECTIVE_2026-10-15_2345UTC.md); and, relayed by IDA about 2026-10-22 01:10 UTC, that "a read counts as full only when its quotes carry src line numbers and verify against the captured file" (artifacts/federal/federal_reviewer_log.md:145).

This report answers the brief IDA sent at 2026-10-28 21:57 UTC (14:57 PDT), which relayed the researcher's instruction: write a PRISMA-style process report on finished work, with no new collection and no change to corpus files, for the folder reports/IDEA_Federal/ of the public repository Choytcudz/Research-Bots.

## 1A. Methodological framework

The work is documentary legal research (Hutchinson & Duncan, 2012) on a corpus of public documents (Bowen, 2009). Coding follows constructivist grounded theory (Charmaz, 2006), extended for legal text: because statutes and regulations are written with action verbs, each provision is coded for actor, action verb, object, trigger, condition and consequence. That scheme is shared with the sibling state bots so the federal rows can be set beside state rows. The federal baseline index codes 120 C.F.R. rows, 17 statute rows and 4 Supreme Court cases (artifacts/federal/Federal_Baseline_Index_2026-10-21.md:9-133, :134-155, :156-166; the case rows are marked TO CODE).

Reporting borrows the structure of PRISMA 2020 (Page et al., 2021) and the search-reporting items of PRISMA-S (Rethlefsen et al., 2021). Grey-literature practice (Adams et al., 2016; Godin et al., 2015) informs how agency guidance was located and labeled. Trustworthiness is handled by an audit trail and peer checking in the sense of Lincoln and Guba (1985): every quote carries a file:line pin, a script checks each quote against its pinned line, and a separate Process Auditor bot audits the trail.

Status vocabulary for each federal counterpart: SUPPLIED, PARTIAL, NONE FOUND (always with the method used) or UNRESOLVED. Absence of a provision is treated as a lead, not a finding. Labels: "agency guidance, not law"; "agency policy, not law"; and "RELATED FEDERAL BASELINE (outside IDEA)" for ESSA, title IV-E and similar material. Keyword-only results are labeled KEYWORD-ONLY.

Sources counted as primary are official hosts only: eCFR, govinfo, uscode.house.gov, ed.gov, supremecourt.gov, loc.gov, acf.gov and acf.hhs.gov, plus Lexis (not used). Cornell LII, Justia, search snippets and recall are not primary; a claim resting on them is UNRESOLVED.

## 2. Timeline

Times come from my log and status files, which are quoted in the appendices. PDT is UTC minus 7 hours. Entries on 2026-10-15 printed local time as "PST" at UTC minus 8 (for example "21:27 UTC / 13:27 PST", federal_reviewer_log.md:47); the PDT column below gives the correct local time, and the source lines are left as written.

| UTC | PDT | Event | Pin |
|---|---|---|---|
| 2026-10-15 20:57 | 2026-10-15 13:57 | IDA brief received; its header prints "12:57 PST" (UTC minus 8) | briefing/BRIEF.md:1 |
| 2026-10-15 21:06 | 2026-10-15 14:06 | Required artifacts checklist saved (status.md:13, project root); its sources were captured by a background worker | artifacts/federal/Federal_Required_Artifacts_Checklist.md:215; federal_reviewer_log.md:48 |
| 2026-10-15 21:26 to 21:27 | 2026-10-15 14:26 to 14:27 | Researcher correction applied: workers stopped, prior items reclassified UNVERIFIED | status.md:48 (root); federal_reviewer_log.md:47-48 |
| 2026-10-15 21:32 to about 23:58 | 2026-10-15 14:32 to about 16:58 | My own reads of eCFR captures, the OSEP letter, provision list; Cornell-only items reclassified UNRESOLVED (22:25) | federal_reviewer_log.md:50, :57, :68, :76, :82, :88 |
| 2026-10-15 23:52 and 23:59 | 2026-10-15 16:52 and 16:59 | Provision list and first-pass state counterpart checks posted | status.md:138, :166 (root) |
| 2026-10-21 21:21 | 2026-10-21 14:21 | Peer review reads begin | federal_reviewer_log.md:91 |
| 2026-10-21 21:22:59 | 2026-10-21 14:22:59 | First govinfo U.S.C. capture | src/usc/CAPTURE_LOG.txt:1 |
| 2026-10-21 22:22:38 | 2026-10-21 15:22:38 | First row of the CFR capture log | src/CFR_CAPTURE_LOG_GA39_56.txt:1 |
| 2026-10-21 22:25 | 2026-10-21 15:25 | Peer review totals recorded (370 cells) | federal_reviewer_log.md:109 |
| 2026-10-21 23:25 to 2026-10-22 00:44 | 2026-10-21 16:25 to 17:44 | Counterpart UPDATE files, coding addenda, further captures | federal_reviewer_log.md:110-139 |
| 2026-10-22 00:39:23 | 2026-10-21 17:39 | HTTP 406 error bodies found and recaptured | src/CFR_CAPTURE_LOG_GA39_56.txt:41 |
| 2026-10-22 01:08:30 to 02:24:09 | 2026-10-21 18:08 to 19:24 | UPDATE12 batches; line-pin ruling noted; record of in-place edits | federal_reviewer_log.md:141-171 |
| 2026-10-22 03:15:06 to 03:28:17 | 2026-10-21 20:15 to 20:28 | Leftover items, DC, UT, NV, GA counterpart files; Supreme Court cases from official sources | federal_reviewer_log.md:173-229 |
| 2026-10-22 03:41:16 | 2026-10-21 20:41:16 | 42 U.S.C. 675a and Pub. L. 113-183 captured | src/usc/CAPTURE_LOG.txt:25-26 |
| 2026-10-22 04:14 | 2026-10-21 21:14 | Last line in artifacts/federal/status.md | artifacts/federal/status.md (Appendix B) |
| 2026-10-22 04:23:31 to 04:52:02 | 2026-10-21 21:23 to 21:52 | NV, DC counterpart batches; guidance captures; IDA browser captures logged | federal_reviewer_log.md:303-357; src/CAPTURE_LOG_guidance.txt:12-26 |
| 2026-10-28 15:55:37 to 15:55:40 | 2026-10-28 08:55 | DC-134 to DC-153 batch and count correction | federal_reviewer_log.md:359-366 |
| 2026-10-28 16:55:06 | 2026-10-28 09:55 | Process Auditor writes the handoff OPEN_FIXES list | audit/handoff/federal/OPEN_FIXES.md:3 |
| 2026-10-28 17:34:42 | 2026-10-28 10:34:42 | Corrections entry R-1: two MEANING FLAG items NOT CLEARED | audit/handoff/federal/OPEN_FIXES.md:41-45 |
| 2026-10-28 21:57 | 2026-10-28 14:57 | IDA brief for this report | IDA message (not in my logs) |
| 2026-10-28 22:02:24 | 2026-10-28 15:02:24 | This report build begins | `date -u` |

An IDA note at 2026-10-28 16:40 UTC (09:40 PDT) passed on four fixes and said not to act until IDA wakes me. They are not done; see section 8.

## 3. Search strategy, searches and direct fetches

No bibliographic database was searched, and Lexis was not used. The corpus was built by direct fetch of known official documents, by within-corpus keyword searches, and on 2026-10-15 by web search run by a background worker.

**Web searches.** The query strings, engines and counts were NOT RECORDED. The only logged trace is that the DC hearing officer determination 2020-0181 was "FOUND via search" from "search snippets" (federal_reviewer_log.md:22; also :37). Those log lines were written by the worker and were reclassified UNVERIFIED (federal_reviewer_log.md:48).

**Direct fetches with a log row.** Every logged fetch is quoted in Appendix C. Counts below are counts of log lines, made with `grep` on 2026-10-28.

| Log | What it records | Count |
|---|---|---|
| src/usc/CAPTURE_LOG.txt | govinfo fetch lines with HTTP 200 (U.S.C. sections, Pub. L. 113-183) | 21 |
| src/usc/CAPTURE_LOG.txt | hash-only lines with no HTTP status (20 U.S.C. 1416 at :17; Pub. L. 108-335 at :24; and companion hash lines) | see Appendix C |
| src/CFR_CAPTURE_LOG_GA39_56.txt | rows naming a cfr file (122 distinct names) | 127 |
| same | of which HTTP 200 stated | 78 |
| same | of which HTTP 404 stated (stub files cfr_229_v2, cfr_2_v2) | 2 |
| same | of which HTTP 406 error bodies, disregarded by the correction at :41 | 4 |
| same | of which no HTTP status recorded (mostly rows 1 to 36) | 43 |
| same | supremecourt.gov bound volumes 546 and 548, HTTP 200 | 2 |
| same | ED/HHS foster care guidance 2016 from acf.hhs.gov, status 200 | 1 |
| src/CAPTURE_LOG_guidance.txt | NRG24 row (2026-10-15 fetch status NOT RECORDED; re-fetch HTTP 403) | 1 |
| same | CAP-1450, CAP-PI1011, CAP-YUD, CAP-200306 rows | 4 |
| same | browser captures fetched by IDA, not by me (NRG24 host match; Letter to Yudien) | 2 |

**Captures with no per-file log row.** The 2026-10-15 captures were not logged file by file. By filename match, 168 of the 288 held `cfr_*.txt` files have no row in the CFR capture log. The OSEP letter, ED/DOJ principles, ED/HHS 2024 guidance and DC HOD captures carry a URL and capture date in their own file headers. The Rowley, Honig, Endrew F. and Fry PDFs each have a provenance file (Appendix C). Fry's URL was first NOT VERIFIED and was verified on 2026-10-21 (src/official/fry_15-497_provenance.txt).

**Within-corpus keyword searches.** These are logged in the text of my log and in counterpart CSV map rows; no single tally was kept, so the total is NOT RECORDED. Every search named in the log:

- Part 300 full text, terms "fundamental", "liberty", "least restrictive means", "rights of the parent" (federal_reviewer_log.md:183).
- Part 300 full text, "classification", "corporal", "handbook", "HIPAA", "cognitive" (federal_reviewer_log.md:197).
- "confinement", "isolation", "seclusion" (federal_reviewer_log.md:203).
- "99.38" and "November" (federal_reviewer_log.md:221).
- "compensatory services" in Part 300 (federal_reviewer_log.md:179).
- Restraint (DC-084) and burden (DC-094), keyword-only (federal_reviewer_log.md:142); restraint and seclusion rows (federal_reviewer_log.md:148).
- 5-A DCMR 3099 for "correctional/incarcerat/jail" (federal_reviewer_log.md:355).
- Utah burden search; the command is recorded in artifacts/federal/Federal_Schaffer_burden_leads_2026-10-22.md:52-53, and an earlier, broader search behind a withdrawn statement was not recorded (same file, line 51).
- Further keyword checks are recorded in counterpart map rows, for example NOTE K-1 (Federal_Counterparts_DC-273-279_2026-10-22.csv:17) and the DC-134 to 153 map rows (Federal_Counterparts_DC-134-153_2026-10-28.csv:23-41). They are not listed one by one here.

The Part 300 full-text file was used for keyword location only (KEYWORD-ONLY).

## 4. PRISMA flow adapted to a documentary corpus

```
IDENTIFICATION
  Bibliographic database records ............................ 0 (none searched)
  Web search queries and hits ................................ NOT RECORDED
  Logged direct-fetch lines, govinfo U.S.C. (HTTP 200) ....... 21
  Logged CFR capture rows ..................................... 127 (122 distinct names)
     HTTP 200 78 | HTTP 404 2 | HTTP 406 error bodies 4 | status not recorded 43
  Other logged fetches (bound volumes 2, NRG 2016 1,
     guidance-log rows 5, IDA browser captures 2) ............. 10
  Captures with no per-file log row (cfr_*.txt by filename) ... 168 of 288

SCREENING (source rule: official hosts only)
  Held in artifacts/federal/src (selected counts)
     cfr_*.txt files .......................................... 288 (206 plain, 82 _v2;
                                                                 211 distinct section names)
     govinfo U.S.C. and Pub. L. pairs in src/usc .............. 22
     Supreme Court: official PDFs 4, bound volumes 2, slip ops 2
     Agency guidance and the DC HOD ........................... see section 5
  Not evidence: Cornell LII copies, U.S.C. ..................... 10  -> UNRESOLVED
  Not evidence: Cornell LII copies, cases ...................... 9   -> UNRESOLVED
     (Schaffer, Arlington later resolved from bound volumes;
      Forest Grove, Burlington, Winkelman remain UNRESOLVED)
  Not captures: HTTP 406 bodies 4, HTTP 404 stubs 2
  Worker output of 2026-10-15 ................................. reclassified UNVERIFIED
                                                                 (count of items NOT RECORDED)

READING
  Read in full vs in part vs keyword-only ..................... recorded per row and per
                                                                 index line; one total
                                                                 NOT RECORDED
  Part 300 full text .......................................... KEYWORD-ONLY

INCLUDED (outputs)
  Federal baseline index ...................................... 120 CFR rows, 17 statute rows,
                                                                 4 cases (TO CODE)
  Counterpart CSV files ....................................... 31
     (method: ls artifacts/federal/Federal_Counterparts*.csv;
      2 further .csv files, the provision list and the
      required artifacts checklist, are not counted)
  Peer review of federal-counterpart cells .................... 370 cells: ACCEPT 172,
                                                                 AWF 46, REJECT 3,
                                                                 UNRESOLVED 6 (227 assessed),
                                                                 no cite 143 (log:109)
```

## 4A. Departures from PRISMA 2020 and PRISMA-S

| Item | Departure | Reason |
|---|---|---|
| Databases and platforms (PRISMA-S 1-2) | None searched | The corpus is primary law and agency documents fetched from official hosts by known citation. |
| Full search strategies (PRISMA-S 8) | Web queries NOT RECORDED | The 2026-10-15 web searching was done by a worker and not logged. |
| Dates of searches (PRISMA-S 13) | Fetch times logged from 2026-10-21; 2026-10-15 captures have dates only | Per-file capture logging began on 2026-10-21. |
| Records identified, duplicates removed (PRISMA 2020 item 16a) | Counts are log lines and files, not records | No search export exists; _v2 recaptures sit beside earlier files. |
| Eligibility criteria (PRISMA 2020 item 5) | Host rule instead of study criteria | The rule is source authority (official host), set by the researcher. |
| Screening by two reviewers (PRISMA 2020 item 8) | Single reviewer, with a separate auditor bot | Team design: one bot per layer; peer review and Process Auditor audits. |
| Risk of bias (PRISMA 2020 items 11, 18) | Not applicable | Legal texts are not studies; source authority and text fidelity are checked instead. |
| Synthesis (PRISMA 2020 items 13, 20) | Coding and counterpart status, not meta-analysis | The question is documentary and legal, not effect sizes. |
| Peer review of search (PRISMA-S 12) | Not done for searches | Search strings were not kept; quotes were checked by script and audit instead. |
| Protocol and registration (PRISMA 2020 item 24) | No registered protocol | Briefs and directives in the project folder serve as the working protocol. |

## 5. Documents held (APA 7)

Government documents and cases are listed by the official copy held. Agency guidance is agency guidance, not law. Items resting only on Cornell LII copies are listed separately as UNRESOLVED and are not evidence.

### 5.1 Statute and session laws (govinfo, United States Code 2024 edition)

- 20 U.S.C. §§ 1232d, 1232g, 1232h (2024). https://www.govinfo.gov/ (captures in src/usc/, Appendix C)
- 20 U.S.C. §§ 1401, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1436 (2024). https://www.govinfo.gov/
- 20 U.S.C. §§ 6311, 6312, 7801 (2024). RELATED FEDERAL BASELINE (outside IDEA). https://www.govinfo.gov/
- 29 U.S.C. § 794 (2024). RELATED FEDERAL BASELINE (outside IDEA). https://www.govinfo.gov/
- 42 U.S.C. §§ 671, 672, 675, 675a (2024). RELATED FEDERAL BASELINE (outside IDEA). https://www.govinfo.gov/
- 42 U.S.C. § 11434a (2024). RELATED FEDERAL BASELINE (outside IDEA). https://www.govinfo.gov/
- District of Columbia Appropriations Act, 2005, Pub. L. No. 108-335, 118 Stat. 1322 (2004). https://www.govinfo.gov/content/pkg/PLAW-108publ335/html/PLAW-108publ335.htm (held as src/plaw108_335.htm; title and page from the capture header, src/plaw108_335.txt)
- Preventing Sex Trafficking and Strengthening Families Act, Pub. L. No. 113-183 (2014). https://www.govinfo.gov/content/pkg/PLAW-113publ183/html/PLAW-113publ183.htm

### 5.2 Regulations (eCFR captures)

- 34 C.F.R. pt. 300 (2026). https://www.ecfr.gov/ (sections held as src/cfr_300.*.txt; full part held for keyword location only)
- 34 C.F.R. pt. 303 (2026). https://www.ecfr.gov/
- 34 C.F.R. pt. 99 (2026), selected sections including § 99.31. https://www.ecfr.gov/
- 34 C.F.R. pt. 104 (2026), selected sections. https://www.ecfr.gov/ RELATED FEDERAL BASELINE (outside IDEA).
- 45 C.F.R. §§ 1355.20, 1356.60 (2026). https://www.ecfr.gov/ RELATED FEDERAL BASELINE (outside IDEA).
- 2 C.F.R. § 200.306 (2026). https://www.ecfr.gov/ RELATED FEDERAL BASELINE (outside IDEA).

Part headings are not given because they were not checked against the captures for this report; the section-level file list is in the handoff manifest (audit/handoff/federal/MANIFEST.tsv). Part 300 and Part 303 captures carry eCFR currency dates in their files.

### 5.3 Cases (official copies)

- Board of Education of the Hendrick Hudson Central School District v. Rowley, 458 U.S. 176 (1982). https://tile.loc.gov/storage-services/service/ll/usrep/usrep458/usrep458176/usrep458176.pdf
- Honig v. Doe, 484 U.S. 305 (1988). https://tile.loc.gov/storage-services/service/ll/usrep/usrep484/usrep484305/usrep484305.pdf
- Schaffer v. Weast, 546 U.S. 49 (2005). In United States Reports, vol. 546 (bound volume). https://www.supremecourt.gov/opinions/boundvolumes/546bv.pdf
- Arlington Central School District Board of Education v. Murphy, 548 U.S. 291 (2006). In United States Reports, vol. 548 (bound volume). https://www.supremecourt.gov/opinions/boundvolumes/548bv.pdf
- Fry v. Napoleon Community Schools, No. 15-497 (U.S. Feb. 22, 2017) (slip opinion). https://www.supremecourt.gov/opinions/16pdf/15-497_p8k0.pdf (reporter citation UNRESOLVED; recorded from memory only in the provenance file)
- Endrew F. v. Douglas County School District RE-1, No. 15-827 (U.S. Mar. 22, 2017) (slip opinion). https://www.supremecourt.gov/opinions/16pdf/15-827_0pm1.pdf (reporter citation UNRESOLVED; recorded from memory only in the provenance file)

### 5.4 Agency guidance (agency guidance, not law) and an administrative decision

- Office of Special Education and Rehabilitative Services. (2014, December 5). *OSEP dear colleague letter on the Individuals with Disabilities Education Act for students with disabilities in correctional facilities*. U.S. Department of Education. https://sites.ed.gov/idea/files/idea-letter.pdf
- U.S. Department of Education & U.S. Department of Justice. (2014, December). *Guiding principles for providing high-quality education in juvenile justice secure care settings*. https://www.ed.gov/sites/ed/files/policy/gen/guid/correctional-education/guiding-principles.pdf
- U.S. Department of Education & U.S. Department of Health and Human Services. (2016, June 23). *Non-regulatory guidance: Ensuring educational stability for children in foster care*. https://www.acf.hhs.gov/ (URL as logged at src/CFR_CAPTURE_LOG_GA39_56.txt; RELATED FEDERAL BASELINE (outside IDEA))
- U.S. Department of Education & U.S. Department of Health and Human Services. (2024, November 15). *Ensuring educational stability and success for students in foster care: Non-regulatory guidance*. https://www.ed.gov/media/document/non-regulatory-guidance-ensuring-educational-stability-and-success-students-foster-care-november-15-2024-108448.pdf
- Administration on Children, Youth and Families, Children's Bureau. (2010, July 9). *Fostering Connections to Success and Increasing Adoptions Act of 2008 (Public Law 110-351) comprehensive guidance* (ACYF-CB-PI-10-11). U.S. Department of Health and Human Services. https://acf.gov/sites/default/files/documents/cb/pi1011.pdf (RELATED FEDERAL BASELINE (outside IDEA))
- Office of Special Education Programs. (2003, August 19). *Letter to Yudien*. U.S. Department of Education. https://sites.ed.gov/idea/files/idea/policy/speced/guid/idea/letters/2003-3/yudien081903fape3q2003.pdf (captured by IDA through the browser; date discrepancy recorded at src/CAPTURE_LOG_guidance.txt:20)
- Office of the State Superintendent of Education, Office of Dispute Resolution. (2020, December 22). *Hearing officer determination, Case No. 2020-0181*. District of Columbia. https://osse.dc.gov/publication/december-2020-hearing-officers-determinations (a state-level decision held in the federal folder; full text NOT read by me per federal_reviewer_log.md:22)

### 5.5 Held but UNRESOLVED (Cornell LII copies, not evidence)

- U.S.C. copies: 20 U.S.C. §§ 1232g, 1401, 1412, 1414, 1415, 1417, 6311, 6312; 42 U.S.C. §§ 671, 675 (superseded in use by the govinfo captures above).
- Case copies: Arlington, Burlington, Endrew F., Forest Grove, Fry, Honig, Rowley, Schaffer, Winkelman. Burlington, Forest Grove and Winkelman have no official copy in the corpus and remain UNRESOLVED.

## 6. Leads

Absence is a lead only. These are open questions, not findings.

1. Whether the D.C. Department of Youth Rehabilitation Services acts as a participating agency for IDEA purposes in the DC rows: UNRESOLVED (see the DYRS handbook rows, for example Federal_Counterparts_DC-114_126-133_2026-10-22.csv:8).
2. Adults in prisons and the D.C. Jail: the scope of 34 C.F.R. 300.102(a)(2) set beside 5-A DCMR 3001.16-17 and the Letter to Yudien; narrowed, not closed (federal_reviewer_log.md:355).
3. The Letter to Yudien date: the text layer reads 2008 while the host page and URL say 2003 (src/CAPTURE_LOG_guidance.txt:20). The reading of 2008 as a misread is INFERENCE.
4. Off-by-one ACYF-CB-PI-10-11 pins in an NV note (audit/handoff/federal/OPEN_FIXES.md:13).
5. Reporter citations for Endrew F. and Fry, and official copies of Burlington, Forest Grove and Winkelman.
6. Whether states may set the burden of proof differently from Schaffer (Federal_Schaffer_burden_leads_2026-10-22.md; the Utah statement stays UNRESOLVED).
7. Conflicts recorded within DC documents in the 2026-10-28 batch, such as records periods of 2 business days against 48 hours, and who appoints a surrogate (federal_reviewer_log.md:364). Recorded, not resolved.

## 7. Limitations

- On 2026-10-15 I delegated almost all reading to a background worker and relayed its summaries as confirmed. After the researcher's correction those items were reclassified UNVERIFIED (federal_reviewer_log.md:47-48). Log lines 1 to 46 are that worker's text.
- Web searches were not logged, and the 2026-10-15 captures have no per-file fetch log.
- No database or Lexis search; some cases rest only on Cornell copies and are UNRESOLVED.
- Some reads are partial or keyword-only; the depth is recorded per row but not totaled.
- On 2026-10-22 some time stamps were typed by hand ahead of the file write (OPEN_FIXES.md:27).
- UPDATE12 was edited in place; the edits are recorded append-only at federal_reviewer_log.md:160-166.
- Single reviewer for the federal layer; the Process Auditor's checks are the second look.
- Two MEANING FLAG items (AWF) on my rows are open (section 8).
- File modification times in the corpus show 2026-10-25 and do not show original write times; the cause is UNRESOLVED.
- Supreme Court case reading covered holding passages in context, not each opinion in full (Federal_Cases_official_2026-10-22.md, Limits).

## 8. Handoff

The handoff package is audit/handoff/federal/: README.md, MANIFEST.tsv, VERIFIED_STATE.md, OPEN_FIXES.md, OPEN_QUEUE.md and STANDING_RULES.md, written by the Process Auditor. OPEN_FIXES.md lists 18 items (OPEN_FIXES.md:39).

Open AWF flags on my rows (both NOT CLEARED under corrections entry R-1):

- Item 1: DC-143 col 6 [QRG:18], omitted tail "and other significant parties." (OPEN_FIXES.md:7, :44).
- Item 12: DC-260 col 6 [S42:22], omitted renewal conditions at S42.ocr lines 22-23 (OPEN_FIXES.md:21, :45).

Other open items: pinpoint items 2, 3, 5, 6, 7, 8, 9, 13, 14 and 15; notes for IDA 4, 10 and 11; open items 16 (21 against 22), 17 (UP-16 missing from the truncation scan output) and 18 (stamps ahead of writes) (OPEN_FIXES.md:8-27).

Held fixes. An IDA note of 2026-10-28 16:40 UTC (09:40 PDT) passed on four fixes and said not to act until IDA wakes me: add the DC-260 renewal conditions in an append-only note; name cfr_300.324_v2.txt for DC-261; delete /tmp copies of the backups after confirming the backups/ hashes; and add a working-directory note to BACKUPS_sha256.txt. They are NOT DONE and stay held, because this report's brief forbids corpus edits.

Also held: DC-154 to 231; UT UP-23 to 44 except UP-35; 2 C.F.R. part 300 and 45 C.F.R. 75.306 captures; the coding queue (audit/handoff/federal/OPEN_QUEUE.md).

## 9. Methods references

Adams, J., Hillier-Brown, F. C., Moore, H. J., Lake, A. A., Araujo-Soares, V., White, M., & Summerbell, C. (2016). Searching and synthesising 'grey literature' and 'grey information' in public health: Critical reflections on three case studies. *Systematic Reviews, 5*(1), Article 164. https://doi.org/10.1186/s13643-016-0337-y

Bowen, G. A. (2009). Document analysis as a qualitative research method. *Qualitative Research Journal, 9*(2), 27-40. https://doi.org/10.3316/QRJ0902027

Charmaz, K. (2006). *Constructing grounded theory: A practical guide through qualitative analysis*. Sage Publications.

Godin, K., Stapleton, J., Kirkpatrick, S. I., Hanning, R. M., & Leatherdale, S. T. (2015). Applying systematic review search methods to the grey literature: A case study examining guidelines for school-based breakfast programs in Canada. *Systematic Reviews, 4*(1), Article 138. https://doi.org/10.1186/s13643-015-0125-0

Hutchinson, T., & Duncan, N. (2012). Defining and describing what we do: Doctrinal legal research. *Deakin Law Review, 17*(1), 83. https://doi.org/10.21153/dlr2012vol17no1art70

Lincoln, Y. S., & Guba, E. G. (1985). *Naturalistic inquiry*. Sage Publications.

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., ... Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, Article n71. https://doi.org/10.1136/bmj.n71

Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., Ayala, A. P., Moher, D., Page, M. J., Koffel, J. B., & PRISMA-S Group. (2021). PRISMA-S: An extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. *Systematic Reviews, 10*(1), Article 39. https://doi.org/10.1186/s13643-020-01542-z

Verification note. On 2026-10-28 between 22:00 and 22:02 UTC (15:00 to 15:02 PDT) each DOI above was looked up at api.crossref.org/works/<doi>; titles, journals, volume, issue, article numbers or pages, years and author lists match the Crossref records. PRISMA 2020 has 26 authors in Crossref; the list follows APA 7 (first 19, ellipsis, last). For PRISMA-S, Crossref lists 41 author entries: the 7 named authors, the PRISMA-S Group, and the group's members; the byline above gives the named authors and the group. Crossref gives only the first page (83) for Hutchinson and Duncan, so no last page is given. Crossref gives no BMJ volume number, so none is given; the volume is UNRESOLVED. The books were checked at openlibrary.org: Charmaz 2006 (work OL4460998W; editions OL8030713M and OL8030714M, Sage, January 27, 2006) and Lincoln and Guba 1985 (work OL16480181W; edition OL2863384M, Sage Publications, Beverly Hills, Calif.). Saldaña (2016), used in the model report, is not cited because Open Library's third-edition record could not be confirmed cleanly.

# Appendices: verbatim quotations with file:line pins

Each line below is copied byte for byte from the named file, prefixed with its path and line number. Nothing inside the code blocks is my prose. Em dashes that appear inside these blocks are in the source files (9 occur in federal_reviewer_log.md: 8 at lines 2, 7, 15, 18, 22, 24, 30 and 37, which a background worker wrote on 2026-10-15, and 1 at line 210 inside a quotation of a federal regulation). Times printed as "PST" on 2026-10-15 are UTC minus 8 as written; section 2 gives the correct PDT.

Not quoted, for privacy or confidentiality: my check-in file (audit/checkin/), rules_audit.md, the researcher's rules files, Design Memo #3, and any personal or case material. Those are described in prose where needed and are not in this repository. Withheld by pin: federal_reviewer_log.md:80 (it describes the researcher's private rules files) and project-root status.md:87 (left out of Appendix D for the same reason).

## Appendix A. Reviewer log (artifacts/federal/federal_reviewer_log.md, all lines)

```
artifacts/federal/federal_reviewer_log.md:1: 
artifacts/federal/federal_reviewer_log.md:2: ## 34 CFR 300.519(d) verification — accessed 2026-10-15
artifacts/federal/federal_reviewer_log.md:3: Source: https://www.ecfr.gov/api/versioner/v1/full/2026-10-13/title-34.xml?part=300&section=300.519 (eCFR current through 2026-10-13 issue date; section last amended 2016-12-19). Web page: https://www.ecfr.gov/current/title-34/subtitle-B/chapter-III/part-300/subpart-E/section-300.519
artifacts/federal/federal_reviewer_log.md:4: 
artifacts/federal/federal_reviewer_log.md:5: Verbatim (d):
artifacts/federal/federal_reviewer_log.md:6: (d) Criteria for selection of surrogate parents. (1) The public agency may select a surrogate parent in any way permitted under State law.
artifacts/federal/federal_reviewer_log.md:7: (2) Public agencies must ensure that a person selected as a surrogate parent—
artifacts/federal/federal_reviewer_log.md:8: (i) Is not an employee of the SEA, the LEA, or any other agency that is involved in the education or care of the child;
artifacts/federal/federal_reviewer_log.md:9: (ii) Has no personal or professional interest that conflicts with the interest of the child the surrogate parent represents; and
artifacts/federal/federal_reviewer_log.md:10: (iii) Has knowledge and skills that ensure adequate representation of the child.
artifacts/federal/federal_reviewer_log.md:11: 
artifacts/federal/federal_reviewer_log.md:12: Verdict: CONFIRMED. The non-employee rule is exactly (d)(2)(i) (no (A) sub-level). (d)(2)(ii) = no conflicting personal/professional interest; (d)(2)(iii) = knowledge and skills for adequate representation.
artifacts/federal/federal_reviewer_log.md:13: Related: (c) judge-appointed surrogates for wards must meet (d)(2)(i) and (e); (e) payment by the agency alone does not make one an employee; (f) temporary surrogates for unaccompanied homeless youth (shelter/transitional/independent-living/outreach staff) are exempt from (d)(2)(i) until a fully qualified one is appointed; (h) SEA must make reasonable efforts to assign within 30 days. Authority: 20 U.S.C. 1415(b)(2).
artifacts/federal/federal_reviewer_log.md:14: 
artifacts/federal/federal_reviewer_log.md:15: ## 2026-10-15 — 34 C.F.R. § 300.503(a) and "DC HOD 2020-0181"
artifacts/federal/federal_reviewer_log.md:16: Accessed 2026-10-15. Source: https://www.ecfr.gov/api/versioner/v1/full/2026-10-13/title-34.xml?part=300&section=300.503 (needs Accept-Encoding/--compressed).
artifacts/federal/federal_reviewer_log.md:17: **Verdict: VERIFIED.** Verbatim § 300.503(a) *Notice.*:
artifacts/federal/federal_reviewer_log.md:18: "Written notice that meets the requirements of paragraph (b) of this section must be given to the parents of a child with a disability a reasonable time before the public agency— (1) Proposes to initiate or change the identification, evaluation, or educational placement of the child or the provision of FAPE to the child; or (2) Refuses to initiate or change the identification, evaluation, or educational placement of the child or the provision of FAPE to the child."
artifacts/federal/federal_reviewer_log.md:19: - Last amended: 2016-12-19 (eCFR versions API, https://www.ecfr.gov/api/versioner/v1/versions/title-34.json?part=300&section=300.503; a later 2023-03-28 issue date is non-substantive).
artifacts/federal/federal_reviewer_log.md:20: - Authority: 20 U.S.C. 1415(b)(3) and (4), 1415(c)(1), 1414(b)(1).
artifacts/federal/federal_reviewer_log.md:21: 
artifacts/federal/federal_reviewer_log.md:22: **DC HOD 2020-0181: FOUND via search; full text NOT read by me.** OSSE page https://osse.dc.gov/publication/december-2020-hearing-officers-determinations lists the Dec. 2020 HODs; search snippets of https://osse-migrate.dc.gov/sites/default/files/dc/sites/osse/publication/attachments/HOD%20December%202020%20%287%29.pdf show: Adult Student v. D.C. Dep't of Youth Rehabilitation Services, Case No. 2020-0181, issued Dec. 22, 2020, Hearing Officer Peter B. Vaden; issues incl. PWN for placement change (June 2019) and IEP change (July 2019); claims re residential-school IEP dismissed as against wrong agency (DCPS responsible); relief denied. My direct PDF fetches failed (HTTP 522 / timeout), so these details are snippet-level only — UNVERIFIED against the full document; the holding on PWN/FAPE is not confirmed. Needs a human/browser read before citing.
artifacts/federal/federal_reviewer_log.md:23: 
artifacts/federal/federal_reviewer_log.md:24: ## 34 CFR 300.503(a) verification (prior written notice) — accessed 2026-10-15 (UTC)
artifacts/federal/federal_reviewer_log.md:25: Source: https://www.ecfr.gov/api/versioner/v1/full/2026-10-13/title-34.xml?part=300&section=300.503 (eCFR; 2026-10-13 is the latest issue date the API accepted). Versions endpoint: https://www.ecfr.gov/api/versioner/v1/versions/title-34.json?part=300&section=300.503
artifacts/federal/federal_reviewer_log.md:26: Last amended: 2016-12-19 (amendment_date of the latest version; the latest issue_date listed is 2023-03-28, which the versions endpoint marks substantive: false).
artifacts/federal/federal_reviewer_log.md:27: Authority cite printed after the section: 20 U.S.C. 1415(b)(3) and (4), 1415(c)(1), 1414(b)(1).
artifacts/federal/federal_reviewer_log.md:28: 
artifacts/federal/federal_reviewer_log.md:29: Verbatim (a):
artifacts/federal/federal_reviewer_log.md:30: (a) Notice. Written notice that meets the requirements of paragraph (b) of this section must be given to the parents of a child with a disability a reasonable time before the public agency—
artifacts/federal/federal_reviewer_log.md:31: (1) Proposes to initiate or change the identification, evaluation, or educational placement of the child or the provision of FAPE to the child; or
artifacts/federal/federal_reviewer_log.md:32: (2) Refuses to initiate or change the identification, evaluation, or educational placement of the child or the provision of FAPE to the child.
artifacts/federal/federal_reviewer_log.md:33: 
artifacts/federal/federal_reviewer_log.md:34: Reading: Timing is "a reasonable time before" the public agency acts; the regulation sets no number of days. Triggers are a proposal or a refusal to initiate or change identification, evaluation, educational placement, or the provision of FAPE. Paragraph (b) lists seven content items; paragraph (c) requires language understandable to the general public and the parent's native language or other mode of communication unless clearly not feasible. All of 300.503(a)-(c) was read.
artifacts/federal/federal_reviewer_log.md:35: Note: "a reasonable time before" is the regulation's wording; do not paraphrase it as a fixed deadline.
artifacts/federal/federal_reviewer_log.md:36: 
artifacts/federal/federal_reviewer_log.md:37: ## DC HOD 2020-0181 search — accessed 2026-10-15 (UTC)
artifacts/federal/federal_reviewer_log.md:38: FOUND (public). D.C. OSSE Office of Dispute Resolution, Hearing Officer Determination, Case No. 2020-0181, Hearing Officer Peter B. Vaden, issued Dec. 22, 2020 (hearing Dec. 15, 2020); Petitioner (an adult student) v. D.C. Department of Youth Rehabilitation Services (DYRS).
artifacts/federal/federal_reviewer_log.md:39: URL (fetched PDF, saved at src/DC_HOD_2020-0181.pdf and .txt): https://osse.dc.gov/sites/default/files/dc/sites/osse/publication/attachments/HOD%20December%202020%20%287%29.pdf . Listing page: https://osse.dc.gov/publication/december-2020-hearing-officers-determinations (file "HOD December 2020 (7).pdf"; the identification of file (7) comes from a search result, and the PDF's own caption matches case no. 2020-0181).
artifacts/federal/federal_reviewer_log.md:40: What the HOD says (read pp. 10-14 of the PDF text; attribution is to the hearing officer, not to a court):
artifacts/federal/federal_reviewer_log.md:41: - The hearing officer cited 34 C.F.R. § 300.503(a) for the rule that written notice must be given a reasonable time before the public agency proposes to change the student's educational placement or the provision of FAPE, and § 300.520(a)(1)(i) for notice to the adult student and parents.
artifacts/federal/federal_reviewer_log.md:42: - The hearing officer found that DYRS placed the student at a residential school beginning April 4, 2019, and that the June 3, 2019 residential school IEP changed a fundamental component of the February 28, 2019 IEP (full-time special education). The hearing officer concluded the IDEA required prior written notice to the student and mother, and that DYRS, not DCPS, had to give it under the MOA because DYRS did not timely notify DCPS. DYRS did not give it to the mother.
artifacts/federal/federal_reviewer_log.md:43: - The hearing officer held the failure was a procedural violation that, under 34 CFR § 300.513(a)(2), could not be deemed a denial of FAPE (mother took part in the placement meetings; no evidence of impeded FAPE right or lost educational benefit).
artifacts/federal/federal_reviewer_log.md:44: - The hearing officer dismissed the claims about the residential school IEP and the PWN at the June 3, 2019 IEP meeting as brought against the wrong agency (DCPS, not DYRS, was responsible); the order denied all relief and dismissed the case.
artifacts/federal/federal_reviewer_log.md:45: Scope: an administrative hearing officer's decision on one record; not precedent for a court. Whether a court reviewed it is UNVERIFIED (the notice of right to appeal cites 20 U.S.C. § 1415(i), 90 days). Citations inside the HOD (e.g., Middleton, Z.B., Shaw) are UNVERIFIED here; IDEA Federal did not check them.
artifacts/federal/federal_reviewer_log.md:46: 
artifacts/federal/federal_reviewer_log.md:47: ## CORRECTION NOTE appended 2026-10-15 21:27 UTC / 13:27 PST (IDEA Federal, after researcher instruction)
artifacts/federal/federal_reviewer_log.md:48: All entries above were produced by a background worker, not by my own reading. Under the researcher correction they are reclassified UNVERIFIED, including the entries marked CONFIRMED or VERIFIED. Entries that rest on Cornell LII, search snippets, or recalled citations are also BLOCKED (official source not yet obtained). The quoted text of 34 C.F.R. 300.519(d) and 300.503(a) may well be correct, but I have not yet re-read the official eCFR text myself. The DC HOD 2020-0181 summary comes from a worker read of a captured PDF and is UNVERIFIED until I read the PDF myself. Original text above is left unchanged. Re-reads will be logged below with UTC and PST times.
artifacts/federal/federal_reviewer_log.md:49: 
artifacts/federal/federal_reviewer_log.md:50: ## SELF RE-READ 2026-10-15 21:32 UTC / 13:32 PST (IDEA Federal, no worker)
artifacts/federal/federal_reviewer_log.md:51: Read myself, in full, the eCFR captures src/cfr_300.519.txt and src/cfr_300.503.txt (html capture carries eCFR data-hierarchy metadata, path /current/title-34/section-300.519 and 300.503; capture came from the earlier worker fetch, capture date 2026-10-15; I did not fetch it myself).
artifacts/federal/federal_reviewer_log.md:52: - 34 C.F.R. 300.519(d)(2)(i): the capture reads "Is not an employee of the SEA, the LEA, or any other agency that is involved in the education or care of the child;". This matches the quote logged above. Status: matches the eCFR capture on my own read; currency date of the capture not independently confirmed by me.
artifacts/federal/federal_reviewer_log.md:53: - 34 C.F.R. 300.503(a): the capture reads as quoted in the entry above; (1) and (2) match; (b) lists seven items and (c) addresses understandable language. Status: matches the eCFR capture on my own read.
artifacts/federal/federal_reviewer_log.md:54: - Limit: I read the saved capture. I did not re-fetch eCFR myself, and I did not check amendment dates myself. The amendment dates in the earlier entries (2016-12-19) remain worker-reported and UNVERIFIED.
artifacts/federal/federal_reviewer_log.md:55: - Not yet read by me: all other cfr_*.txt captures, usc*.txt (Cornell, unofficial, BLOCKED), case texts (Cornell, unofficial, BLOCKED), DC HOD, and the three guidance captures.
artifacts/federal/federal_reviewer_log.md:56: 
artifacts/federal/federal_reviewer_log.md:57: ## SELF READ: OSEP Dear Colleague Letter, Dec. 5, 2014 (correctional facilities) 2026-10-15 21:45 UTC / 13:45 PST
artifacts/federal/federal_reviewer_log.md:58: Source file: src/OSEP_DCL_Correctional_Facilities_2014-12-05.txt, a browser capture (capture date 2026-10-15) of https://sites.ed.gov/idea/files/idea-letter.pdf, an official ed.gov host. I read all 20 letter pages and the resources page myself, line by line, with no worker. I did not compare the text capture against the PDF image. Signatories as printed: Melody Musgrove, Director, OSEP, and Michael K. Yudin, Acting Assistant Secretary, OSERS.
artifacts/federal/federal_reviewer_log.md:59: What the letter says that bears on the checklist (attribution is to the Department, not to a court; the letter is guidance, not a regulation):
artifacts/federal/federal_reviewer_log.md:60: - Footnote 10 states that 34 CFR 300.102(a)(2)(i) addresses ages 18 through 21 in adult correctional facilities and that 300.324(d) covers students convicted as adults and incarcerated in adult prisons. This agrees with the errata I sent (300.324(d) is adult prisons; 300.102(a)(2) is the adult-corrections exception). The letter's own page 5 note says "(34 CFR §300.324(d)(1)(ii))" for transition in adult prisons (footnote 30).
artifacts/federal/federal_reviewer_log.md:61: - The letter names 300.154(a) as the source for the interagency agreement requirement (three required subjects: financial responsibility with reimbursement terms, dispute resolution, coordination and delivery of services) and 300.154(b)(2) for LEA or State agency fallback payment with reimbursement claims.
artifacts/federal/federal_reviewer_log.md:62: - Surrogate parents: the letter cites 300.519(a), (b), (c), (d), (e), (g), (h) and states the 30-day reasonable-efforts duty falls on the SEA. It says a correctional facility may not act as the parent. Its statutory cite for unaccompanied homeless youth is printed "42 U.S.C. §11434(a)(6)", while the eCFR capture of 300.519(a)(4) prints "42 U.S.C. 11434a(6)". The two differ; I have not checked the U.S. Code myself.
artifacts/federal/federal_reviewer_log.md:63: - Records: new agency must take reasonable steps to obtain records and the previous agency must respond (300.323(g)); FERPA exception cited as 34 CFR 99.31(a)(2) and 99.34 (footnote 23). The letter says 99.31(a)(2) is the exception most relevant to records going to a facility.
artifacts/federal/federal_reviewer_log.md:64: - Notice: PWN under 300.503 and procedural safeguards notice under 300.504, and 300.520(a)(1)(i), reach parents of students in facilities.
artifacts/federal/federal_reviewer_log.md:65: Candidate inconsistencies inside the letter (internal, not mine): footnote 29 refers to "fn. 11" for the 18 to 21 exception, but that discussion is in footnote 10 on the capture; footnote 28 cites 300.324(d)(2) for the security modification while footnote 10 describes the modification as the third item of 300.324(d). I did not resolve these against the regulation yet; I will re-read 300.324 myself first.
artifacts/federal/federal_reviewer_log.md:66: Not established by this read: whether this letter has been superseded or rescinded (the capture header says the landing page was last modified Oct. 24, 2023, which I did not independently check). Unresolved.
artifacts/federal/federal_reviewer_log.md:67: 
artifacts/federal/federal_reviewer_log.md:68: ## SELF READ: 34 CFR 300.324 and 300.102, eCFR captures 2026-10-15 21:52 UTC / 13:52 PST
artifacts/federal/federal_reviewer_log.md:69: Read myself, in full: src/cfr_300.324.txt and src/cfr_300.102.txt (eCFR html captures; I did not re-fetch). Capture footers show 300.324 "[71 FR 46753, Aug. 14, 2006, as amended at 82 FR 29761, June 30, 2017]" and 300.102 "as amended at 82 FR 29759, June 30, 2017".
artifacts/federal/federal_reviewer_log.md:70: - 300.324(c) is titled "Failure to meet transition objectives": (c)(1) a participating agency other than the public agency fails to provide transition services in the IEP, and the public agency must reconvene the IEP Team to identify alternative strategies. This supports the errata that the transition-failure rule is 300.324(c).
artifacts/federal/federal_reviewer_log.md:71: - 300.324(d) is titled "Children with disabilities in adult prisons": (d)(1) lists requirements that do not apply (general assessments; transition under 300.320(b) for those whose eligibility ends by age before release eligibility); (d)(2) allows IEP Team modification of IEP or placement on a demonstrated bona fide security or compelling penological interest, with 300.320 and 300.114 not applying to those modifications. It applies only to children convicted as adults and incarcerated in adult prisons. Supports the errata.
artifacts/federal/federal_reviewer_log.md:72: - 300.102(a)(2) concerns children aged 18 through 21 and incarceration in an adult correctional facility: (i) exception where State law does not require services for those not identified and without an IEP in the last placement before incarceration; (ii) exception does not apply if identified and served under an IEP who left school before incarceration, or identified without an IEP in last setting. Supports the errata that 300.102(a)(2) is the adult-corrections age exception. Note (a)(3)(iii): graduation with a regular diploma is a change in placement requiring written prior notice under 300.503.
artifacts/federal/federal_reviewer_log.md:73: - The OSEP 2014 letter footnotes 10 and 28 are consistent with this text. The letter's footnote 29 cross-reference to "fn. 11" appears to be a letter-internal mismatch (the discussion is in footnote 10); unresolved and not mine to correct.
artifacts/federal/federal_reviewer_log.md:74: - Status: errata items 1 and 2 (300.324(c)/(d); 300.102(a)(2)) now match the eCFR captures on my own read. Errata items on 300.155/.149/.154 and FERPA 99.31 vs 1232g(b)(1)(L) are NOT yet re-read by me. Official U.S.C. text for 1232g is BLOCKED pending IDA's uscode.house.gov capture.
artifacts/federal/federal_reviewer_log.md:75: 
artifacts/federal/federal_reviewer_log.md:76: ## STATUS RECLASSIFICATION 2026-10-15 22:25 UTC / 14:25 PST (IDEA Federal)
artifacts/federal/federal_reviewer_log.md:77: Researcher correction relayed by IDA: secondary sources such as Cornell LII may supplement but are never the primary or only source for any item. Applied:
artifacts/federal/federal_reviewer_log.md:78: - Items resting only on Cornell LII copies (src/usc*.txt for 20 USC 1401, 1412, 1414, 1415, 1417, 1232g, 20 USC 6311, 6312, 42 USC 671, 675; src/ case texts for Schaffer, Forest Grove, Arlington, Winkelman, Burlington; and any checklist row whose only statutory or case source was a Cornell page) are UNRESOLVED. Official capture needed: uscode.house.gov or govinfo.gov (U.S. Code), supremecourt.gov or loc.gov U.S. Reports, or Lexis.
artifacts/federal/federal_reviewer_log.md:79: - Rowley, Honig, Endrew F. now have official captures in src/official/ (loc.gov for Rowley and Honig; supremecourt.gov slip opinion for Endrew F.). I have not yet read them myself, so they remain UNVERIFIED until I do. Fry: official source URL unresolved. Reporter cites for Endrew F. (580 U.S. 386) and Fry (580 U.S. 154) were from memory in IDA's provenance files and the earlier worker pass; they are UNRESOLVED and are not to be used until read from an official page.
artifacts/federal/federal_reviewer_log.md:80: [withheld: describes the researcher's private rules files]
artifacts/federal/federal_reviewer_log.md:81: 
artifacts/federal/federal_reviewer_log.md:82: ## SELF READ batch 2026-10-15 ~23:50 UTC (16:50 PDT), IDEA Federal, no workers
artifacts/federal/federal_reviewer_log.md:83: Captured from eCFR API (issue date 2026-10-13) into src/ as cfr_*.txt and .xml: 300.1, .2, .4, .5, .8, .9, .13, .15, .17, .19, .20, .27, .28, .29, .31, .34, .36, .39, .40, .41, .42, .43, .44, .112, .115, .116, .117, .156, .160, .174, .208, .303, .325, .328, .600, .640, .700, .704. 300.18 and .35 returned no text (likely reserved); not read.
artifacts/federal/federal_reviewer_log.md:84: Read in full by me: 300.1, 300.2, 300.4, 300.9, 300.28, 300.30, 300.40, 300.45, 300.209, 300.300, 300.322, 300.323, 300.520. 300.321 was only partly read (tool output truncated the middle); not claimed as read.
artifacts/federal/federal_reviewer_log.md:85: Not read yet: all other captured files. Statutes remain UNRESOLVED.
artifacts/federal/federal_reviewer_log.md:86: Output: artifacts/federal/Federal_Provision_List.md and .csv (52 rows; 13 READ, rest marked NOT YET READ BY ME or UNRESOLVED).
artifacts/federal/federal_reviewer_log.md:87: 
artifacts/federal/federal_reviewer_log.md:88: ## SELF READ 2026-10-15 ~23:58 UTC (16:58 PDT): 300.321 (all), 300.300 (all, second read), 300.519 (second read), 300.301(a)-(c), 300.320(b)-(c), 300.45, 300.209
artifacts/federal/federal_reviewer_log.md:89: Output: Federal_Counterpart_Checks_GA_UT_DC.md; appended update to the NV first-pass file (300.301(c)(1) correction).
artifacts/federal/federal_reviewer_log.md:90: 
artifacts/federal/federal_reviewer_log.md:91: ## 2026-10-21 21:21 UTC / 14:21 PDT: peer review reads (appended)
artifacts/federal/federal_reviewer_log.md:92: Read in full myself from eCFR captures (artifacts/federal/src): 300.2, .28, .34, .45, .101, .151-.153, .300(b)(4) recheck, .301, .303-.311, .320, .324, .325, .328, .501, .502, .504, .506-.518, .530-.536, .600, .610-.626, .640, .704; 99.31. Partial: 99.3 (PII entry only). Used to assign verdicts to 370 federal-counterpart cells; see peer_review/IDEA_Federal_counterpart_review.md.
artifacts/federal/federal_reviewer_log.md:93: 
artifacts/federal/federal_reviewer_log.md:94: - 2026-10-21 21:25 UTC / 14:25 PDT: Captured govinfo USCODE 2024 Edition to artifacts/federal/src/usc/ (htm + txt; CAPTURE_LOG.txt). Read in full: 20 USC 1401, 1412, 1413, 1414, 1415, 1417, 1418, 1436, 1232g, 7801; 42 USC 675, 11434a. Captured, not yet read: 42 USC 671; 20 USC 6311, 6312. Appended U.S.C. resolutions to the review (10 cells resolved; UNRESOLVED 34 to 24).
artifacts/federal/federal_reviewer_log.md:95: - 2026-10-21 21:25 UTC / 14:25 PDT: Read in full 42 USC 671 (2024 Ed., lines 1-479 incl. notes). Leads for corpus (reconstruction only): (a)(8) use/disclosure safeguards; (a)(9)(C) policies developed in consultation with "juvenile justice systems ... education agencies" (sex trafficking, Pub. L. 113-183); (a)(16) case plan per 675(1); (a)(30) assurance that each school-age child eligible for payment is a full-time elementary or secondary school student or has completed secondary school (Pub. L. 110-351 §204(b)); (a)(37) certification that the State "will not enact or advance policies or practices that would result in a significant increase in the population of youth in the State's juvenile justice system" (Pub. L. 115-123 §50741(d)(1), eff. Oct. 1, 2019 with up to 2-year State delay option); (c) public access to court proceedings. So-in-original notes 2 and 3 recorded.
artifacts/federal/federal_reviewer_log.md:96: - 2026-10-21 21:26 UTC / 14:26 PDT: Read in full 20 USC 6311 (2024 Ed., 624 lines incl. notes) and 20 USC 6312 (155 lines). Leads (reconstruction only): 6311(g)(1)(E)(i)-(iv) SEA collaboration with the State title IV-B/IV-E agency for educational stability of children in foster care (school of origin unless not in best interest; immediate enrollment without records; enrolling school contacts last school; SEA foster care point of contact, not the McKinney-Vento coordinator); 6311(g)(1)(C)(ii)-(iii) reducing overuse of exclusionary discipline and aversive interventions; 6311(h)(1)(C)(ii)-(iii) report card disaggregation by homeless status and "status as a child in foster care"; (h)(1)(C)(viii)(I) school-related arrests and referrals to law enforcement; 6311(i) privacy per 1232g; 6311(b)(2)(D) 1 percent alternate assessment cap, IEP team determines participation. 6312(b)(5) services for children in local institutions for neglected or delinquent children; (b)(6) homeless; (b)(11) discipline; (c)(5)(A)-(B) LEA collaboration with child welfare agency: point of contact and written transportation procedures by 1 year after Dec. 10, 2015, consistent with 42 USC 675(4)(A), cost options (I)-(III). So-in-original notes: 6311 notes 1-7 (incl. "1412(c)(16)(C)" probably 1412(a)(16)(C)); 6312 notes 1-2. All 15 captured U.S.C. sections now read in full.
artifacts/federal/federal_reviewer_log.md:97: - 2026-10-21 21:26 UTC / 14:26 PDT: Fry v. Napoleon slip opinion (No. 15-497) on disk verified byte-identical to supremecourt.gov 15-497_p8k0.pdf (HTTP 200, 21:26:17Z, SHA-256 match). Provenance file appended.
artifacts/federal/federal_reviewer_log.md:98: - 2026-10-21 21:26 UTC / 14:26 PDT: Read Fry slip opinion in full (26 pp.); reading note at notes/case_fry_15-497_reading_note.md. Case PDFs read: 1 of 4.
artifacts/federal/federal_reviewer_log.md:99: - 2026-10-21 21:27 UTC / 14:27 PDT: Read Endrew F. slip opinion in full (20 pp.); note at notes/case_endrew_f_15-827_reading_note.md. Case PDFs read: 2 of 4.
artifacts/federal/federal_reviewer_log.md:100: - 2026-10-21 21:28 UTC / 14:28 PDT: Read Honig v. Doe, 484 U.S. 305, in full (38 pp., incl. concurrence and dissent); note at notes/case_honig_484us305_reading_note.md. Case PDFs read: 3 of 4.
artifacts/federal/federal_reviewer_log.md:101: - 2026-10-21 21:28 UTC / 14:28 PDT: Read Rowley, 458 U.S. 176, in full (43 pp., incl. concurrence and dissent); note at notes/case_rowley_458us176_reading_note.md. Case PDFs read: 4 of 4. Batch complete.
artifacts/federal/federal_reviewer_log.md:102: - 2026-10-21 21:31 UTC / 14:31 PDT: Read in full 34 CFR 300.8, .17, .33, .111, .114, .116, .149, .154, .155 (eCFR captures; errata items for .149/.154/.155 can now be checked). Supplied federal counterparts for 85 rows (UT v2 23, NV JJ 22, DC 41-80 40): SUPPLIED 47, PARTIAL 18, NONE FOUND 17, UNRESOLVED 3.
artifacts/federal/federal_reviewer_log.md:103: - 2026-10-21 21:34 UTC / 14:34 PDT: Captured and read in full 300.37, .104, .115, .156, .627, 99.38 (eCFR API 2026-10-13) and 29 USC 794 (govinfo USCODE-2024). SHA-256: 300.37 2a48ac9c..., 300.104 f3af0891..., 300.115 76b47ede..., 300.156 3fb63c31..., 300.627 ef29316e..., 99.38 4afd092f..., 794 htm 5afb14b2.... Counterpart update: UPDATE1.csv; UNRESOLVED now 1 (UP-08).
artifacts/federal/federal_reviewer_log.md:104: - 21:34 UTC: re-capture of 300.115/.156/.627 word-identical to earlier captures (only a leading blank line differs); duplicates removed.
artifacts/federal/federal_reviewer_log.md:105: - 2026-10-21 21:35 UTC / 14:35 PDT: UT v3 UJ-15..17 counterparts appended (UPDATE2.csv): 0 supplied, 2 partial, 1 none found.
artifacts/federal/federal_reviewer_log.md:106: - 2026-10-21 21:36 UTC / 14:36 PDT: Captured and read in full 34 CFR 300.22 and 99.3 (full). UPDATE3.csv written. 99.8 not read.
artifacts/federal/federal_reviewer_log.md:107: - 2026-10-21 21:39 UTC / 14:39 PDT: Captured and read in full 34 CFR 99.8, 104.33-.36. UPDATE4.csv (UJ-16, UJ-18 new, NV-JJ-006 Part 104). 104.3 not read.
artifacts/federal/federal_reviewer_log.md:108: - 2026-10-21 21:48 UTC / 14:48 PDT: Marked IDEA_Federal_reviews_counterparts.md and IDEA_Federal_reviews_state_matrices.md as superseded snapshots (mtime 21:25:34 UTC); count reconciliation appended to canonical review (229 assessed; U=24).
artifacts/federal/federal_reviewer_log.md:109: - 2026-10-21 22:25 UTC / 15:25 PDT: Reassessed GA-39..GA-56 against 34 CFR (new captures 300.7,.10,.23,.105,.106,.108,.109,.113,.119,.175,.221,.227,.601,.641,.645; 20 USC 1416). A4/AWF12/NC2. Totals now A172/AWF46/R3/U6 = 227 assessed, NC143, 370 cells. GA rule text not read by me; verdicts rest on IDEA Georgia's quotes.
artifacts/federal/federal_reviewer_log.md:110: - 2026-10-21 23:25 UTC / 16:25 PDT: (1) UPDATE5.csv written: 40 NV L2 rows (NV-L2-001..040), SUPPLIED 6 / PARTIAL 19 / NONE FOUND 15; UNRESOLVED points inside rows: 300.302 not read, MOUs and Attachments A/B not in hand, NRS sections not read. Re-read in full this turn: 300.2, .13, .17, .22, .30, .39, .43, .45, .101, .104, .301, .323, .503, .519, .530, .610, .622; excerpts only of .114, .116, .154, .320, .324, .102, .8, 99.31, 42 USC 675, 1232g. Row NV-L2-007 prints '(300.13)' for Confinement; 34 CFR 300.13 is 'Elementary school' (inference: Nevada policy number; IDEA Nevada to confirm). (2) Appended IDEA Georgia's answers on GA-41/47/45 and the GA-41 'previous LEA' vs 'previous public agency' comparison item to the canonical review; counts unchanged. (3) Created Federal_Baseline_Index_2026-10-21.md: 120 CFR lines (32 coded from text re-read now, 88 TO CODE), 17 statutes and 4 cases TO CODE. Read in full now: 300.7, .23, .105, .106, .108, .109, .113, .119, .175, .221, .227, .601, .641, .645. 20 USC 1416 read-in-full status not stated in log: VERIFY.
artifacts/federal/federal_reviewer_log.md:111: - 2026-10-21 23:26 UTC / 16:26 PDT: Correction note written (Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE5_correction.md): NV-L2-007 '(300.13)' is Nevada DCFS/JJS 300.13 (Confinement) per IDEA Nevada, not JJS 500.13 as I inferred. Status and 300.530 comparison unchanged.
artifacts/federal/federal_reviewer_log.md:112: 
artifacts/federal/federal_reviewer_log.md:113: ## 2026-10-21 23:31 UTC / 16:31 PDT
artifacts/federal/federal_reviewer_log.md:114: - UPDATE6 written: Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE6.csv (SHA-256 71353f0fd658c762...). UT v3 rows UJ-19..UJ-38: SUPPLIED 5, PARTIAL 13, NONE FOUND 2. UNRESOLVED inside rows: 34 CFR 99.4 (UJ-20), 20 USC 1232h (UJ-37), not captured.
artifacts/federal/federal_reviewer_log.md:115: - 34 CFR 300.302 captured (eCFR versioner, 2026-10-13; xml SHA-256 09fae1e0d8720cdb...) and read in full. NV-L2-002 point closed by append to UPDATE5_correction.md; row stays PARTIAL.
artifacts/federal/federal_reviewer_log.md:116: - Baseline index: 88 CFR lines coded from full re-reads; all 120 CFR lines CODED. 20 USC 1416 VERIFY resolved (read in full). Statutes (17) and cases (4) still TO CODE. Index SHA-256 now 303dd21146fa2c53...
artifacts/federal/federal_reviewer_log.md:117: 
artifacts/federal/federal_reviewer_log.md:118: ## 2026-10-22 00:22 UTC / 17:22 PDT, IDEA Federal
artifacts/federal/federal_reviewer_log.md:119: - UPDATE7 written: Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE7.csv (sha256 ae0a9bf9a8ab4375...), UT v3 rows UJ-39 to UJ-76 (38 rows): SUPPLIED 18, PARTIAL 18, NONE FOUND 2 (UJ-42 dual enrollment, UJ-58 restraint/seclusion). Every quoted federal string checked programmatically against captured text (93 quoted strings, all found). Comparison items, not findings.
artifacts/federal/federal_reviewer_log.md:120: - Mapping checks requested by IDA: III.C.1.b (UJ-69) to 300.323(e) verified; 300.323(f) is interstate and not supplied. IV.U.2 (UJ-63) to 300.520(a)(2) verified (permissive; (a)(2) sits under the age-of-majority lead-in, structural note recorded). VI.K (UJ-71) to 300.2(b)(1)(iv) only partly fits (correctional facilities); added 300.2(b)(1)(iii), .101(a), .111, .114(a)(2)(i), .154. II.C.1.b (UJ-67) maps to 300.300(a)(2), not 300.519. Disagreements recorded, not resolved.
artifacts/federal/federal_reviewer_log.md:121: - New captures, read in full: 34 CFR 300.162, .167, .168, .169, .200, .201, .202, .203, .327, 99.4, 99.22 (eCFR 2026-10-13; logged in src/CFR_CAPTURE_LOG_GA39_56.txt); 20 U.S.C. 1232h (govinfo USCODE-2024; logged in src/usc/CAPTURE_LOG.txt).
artifacts/federal/federal_reviewer_log.md:122: - UJ-20 (99.4) and UJ-37 (1232h) UNRESOLVED points closed by append-only notes in Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE6_correction.md (sha256 e17639674d42ba2d...). UPDATE6 not edited. Statuses unchanged (UJ-20 SUPPLIED, UJ-37 PARTIAL).
artifacts/federal/federal_reviewer_log.md:123: - Index: 300.621 note on 99.22 closed by appended change note (Federal_Baseline_Index_2026-10-21.md sha256 543c043736b9abab...).
artifacts/federal/federal_reviewer_log.md:124: - GA currency lead logged: GA 160-4-7-.21(12) brackets 34 CFR 300.10; src/cfr_300.10.txt (eCFR 2026-10-13, xml sha256 33b3c8181e8b87fb...) reads in full: "§ 300.10 [Reserved]". Comparison item on currency only, not a finding; already noted at peer_review/IDEA_Federal_counterpart_review.md lines 509, 523.
artifacts/federal/federal_reviewer_log.md:125: - Still open: 34 CFR 300.165 (UJ-76), 300.602-.608, 300.130-.144 other than .130/.137, 104.3; ESEA Title I-D text (UJ-49); coding of 17 statutes and 4 cases in the index (next).
artifacts/federal/federal_reviewer_log.md:126: 
artifacts/federal/federal_reviewer_log.md:127: ## 2026-10-22 00:33 UTC / 17:33 PDT, IDEA Federal
artifacts/federal/federal_reviewer_log.md:128: - IDEA DC disagreements answered (appended to peer_review/IDEA_Federal_counterpart_review.md and Federal_Counterparts_UT_NV_DC_2026-10-21.md): DC-049, IDEA DC correct, 300.301(b) reads 'either a parent of a child or a public agency may initiate a request'; my 'State agency or LEA' paraphrase was inaccurate; corrected note recorded, status SUPPLIED unchanged. DC-077, MOA VI.C.4 designates the letter as prior written notice; compared with 300.503(b)-(c), text read names only 'the information used to make the decision' (partial match to (b)(3)); recipient and timing comparison items; status PARTIAL unchanged. MOA read: lines 415-440 only.
artifacts/federal/federal_reviewer_log.md:129: - UPDATE8 written: Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE8.csv (sha256 c12c46a29cd52017...), UJ-77 to UJ-80: SUPPLIED 3 (UJ-78, -79, -80; 300.151-.153), NONE FOUND 1 (UJ-77 DCFS MIS). 24 quoted strings checked against captured text, all found.
artifacts/federal/federal_reviewer_log.md:130: - Captured and read in full: 34 CFR 300.165, 300.602-.608, 104.3. Notes appended: UPDATE7_correction.md (sha256 e6203453bf4534ea...; UJ-76 300.165 closed, 1232d(b)(7) UNRESOLVED; UJ-41 adds 300.608; UJ-70 adds 300.607) and NV-JJ-006 104.3 note in Federal_Counterparts_UT_NV_DC_2026-10-21.md.
artifacts/federal/federal_reviewer_log.md:131: - Next: index coding of 17 statutes and 4 cases.
artifacts/federal/federal_reviewer_log.md:132: - 2026-10-22 00:33 UTC / 17:33 PDT: Index coding addendum appended: 300.165, 300.602-.608, 104.3, 20 U.S.C. 1417, 1436, 42 U.S.C. 11434a coded from full re-reads this turn. 15 statutes and 4 cases still TO CODE.
artifacts/federal/federal_reviewer_log.md:133: - 2026-10-22 00:34 UTC / 17:34 PDT: Captured and read in full 20 U.S.C. 1232d (govinfo). UJ-76 1232d(b)(7) point closed in UPDATE7_correction.md (60/30 days in (b)(7)(B)); status PARTIAL unchanged.
artifacts/federal/federal_reviewer_log.md:134: - 2026-10-22 00:36 UTC / 17:36 PDT: Captured 20 U.S.C. 1232d. Index addendum 2 coded from full re-reads: 1232d, 1418, 794, 1416, 1413, 1401, 1232g, 1232h, 6312, 675, 1414, 1415. DC-049 supplement appended (1414(a)(1)(B) vs 300.301(b) wording). Remaining: 1412, 7801, 671, 6311; four cases; IDA DC 5-A30 request queued.
artifacts/federal/federal_reviewer_log.md:135: - 2026-10-22 00:37 UTC / 17:37 PDT: Addendum 2 statute coding complete from full re-reads: added 1412, 7801, 671, 6311 (after 675, 1414, 1415). Index sha16 ee90c09b69e57d8d. Quotes spot-verified against src. Next: four cases (Fry, Endrew F., Honig, Rowley), then IDA DC 5-A30 UPDATE9 and DC rows 41-80 response.
artifacts/federal/federal_reviewer_log.md:136: - 2026-10-22 00:38 UTC / 17:38 PDT: Addendum 2 case coding complete from full re-reads of official text: Endrew F. (slip op.), Fry (slip op.), Honig (484 U.S. 305), Rowley (458 U.S. 176). Quotes verified against src. Text notes: Fry src 'words(?)' artifact; Honig OCR lacks most page numbers (syllabus ranges used); U.S. Reports cites for Endrew F. and Fry remain from memory, unverified. Index sha16 408782a28eed9ddc. Next: IDA DC 5-A30 counterpart request (UPDATE9) and DC rows 41-80 response.
artifacts/federal/federal_reviewer_log.md:137: - 2026-10-22 00:41 UTC / 17:41 PDT: IDA 5-A30 request done. eCFR recapture 300.300, 300.324, 300.33, 300.8 (version 2026-10-13; first attempt returned HTTP 406, logged and corrected in CFR_CAPTURE_LOG). UPDATE9 (4 rows, sha16 cd14d2657a87d2d9). Response to IDEA DC rows 41-80 review: peer_review/IDEA_Federal_response_DC_rows41-80_2026-10-22.md, including a correction to my DC-078 675(1)(G) lead.
artifacts/federal/federal_reviewer_log.md:138: - 2026-10-22 00:42 UTC / 17:42 PDT: IDA 00:40Z requests done: UPDATE10 (3 rows, sha16 66265b4666dce91e): 300.530(i) definitions, 300.535 NONE FOUND in 3043, expert fees PARTIAL with Arlington UNRESOLVED (no official copy). Response file addendum appended.
artifacts/federal/federal_reviewer_log.md:139: - 2026-10-22 00:44 UTC / 17:44 PDT: IDA 00:43 items done. Index correction note: Endrew F. and Fry reporter cites UNRESOLVED (slip-op cites only; queue with Arlington). Captured and read 42 USC 672 (govinfo), 45 CFR 1355.20 (eCFR), Pub. L. 108-335 sec. 327 (govinfo). UPDATE11 (2 rows, sha16 62dfdac81b2471f5). Official/Lexis queue: Arlington No. 05-18; Endrew F. No. 15-827 and Fry No. 15-497 U.S. Reports pages. Next: coding queue.
artifacts/federal/federal_reviewer_log.md:140: 
artifacts/federal/federal_reviewer_log.md:141: ## UPDATE12 batches 1-2 (2026-10-22T01:08:30Z / 2026-10-21 18:08 PDT)
artifacts/federal/federal_reviewer_log.md:142: File: Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE12.csv, sha16 349a81a3add3dbed. 18 rows: DC-081 to DC-097 plus 3001.16-17 (IDA request). PARTIAL 8, SUPPLIED 6, NONE FOUND 4 (two keyword-only: DC-084 restraint, DC-094 burden). New captures: 300.45, 300.151, 300.152, 300.153 (read: 300.45, 300.153); full Part 300 for keyword search only. All quotes verified against src files. Schaffer (DC-094) UNRESOLVED, no official copy. Batches 3-4 (DC-098 to DC-125, 300.208, .156/.138, .115(b)(1), .306(b), FERPA, .33 respondents) not yet done.
artifacts/federal/federal_reviewer_log.md:143: 
artifacts/federal/federal_reviewer_log.md:144: ## Ruling noted and line map (2026-10-22T02:17:28Z / 2026-10-21 19:17 PDT)
artifacts/federal/federal_reviewer_log.md:145: Researcher's ruling, as relayed by IDA (about 01:10 UTC): a read counts as full only when its quotes carry src line numbers and verify against the captured file. From now on every quote carries file:line. Quotes that drop words use an ellipsis, and altered text uses brackets (APA 7). Created UPDATE12_quote_line_map_2026-10-22.md (sha16 f945186e37ee0c0b). It line-maps every UPDATE12 batch 1-2 quote, plus the three items the Process Auditor marked UNRESOLVED (the DC review, 42 U.S.C. 672 and 45 CFR 1355.20). Correction note: the DC-086 and DC-088 CSV quotes join list lines; the verified item-by-item form is in the map.
artifacts/federal/federal_reviewer_log.md:146: 
artifacts/federal/federal_reviewer_log.md:147: ## UPDATE12 batch 3 (2026-10-22T02:18:23Z / 2026-10-21 19:18 PDT)
artifacts/federal/federal_reviewer_log.md:148: Appended 6 rows (DC-098, DC-099, DC-101, DC-102, DC-103, DC-104) to Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE12.csv, now sha16 cd7e5f0f95714c50, 24 rows. PARTIAL 4 and NONE FOUND 2; both NONE FOUND rows (restraint, seclusion) are keyword-only. DC-100 was answered earlier (UPDATE10). New capture: 300.536 (read in full). Line-cite key for these rows: [530:n] = src/cfr_300.530_v2.txt line n; [536:n] = src/cfr_300.536_v2.txt; [3043:n], [3044:n], [3045:n] = reviews/DC/raw/5-A30xx_text_20261022.txt. Every bracketed quote was checked by script against the cited lines; 0 mismatches.
artifacts/federal/federal_reviewer_log.md:149: 
artifacts/federal/federal_reviewer_log.md:150: ## UPDATE12 batch 4a (2026-10-22T02:19:51Z / 2026-10-21 19:19 PDT)
artifacts/federal/federal_reviewer_log.md:151: Appended 9 rows (DC-105 to DC-113) to Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE12.csv, now sha16 b9b01cbc87443cc2, 33 rows. New captures, all read in full where cited: 300.114, .300 (para (c) only), .303, .306, .310, .323, .34 (paras (a) and (c)(5) only), .106. Line-cite key: [NNN:n] = src/cfr_300.NNN_v2.txt line n, except [115:n] = src/cfr_300.115.txt; [30xx:n] = reviews/DC/raw/5-A30xx_text_20261022.txt. Each quote was checked by script against a cited line range in its row; 0 failures after one cite was added to DC-113. DC-108 also rests on a keyword-only search of the full Part 300 ("licensed physician").
artifacts/federal/federal_reviewer_log.md:152: Correction (2026-10-22T02:20:00Z / 2026-10-21 19:20 PDT): in DC-108 and DC-109 the source cells for 300.34 and 300.300 originally said "read in full". They now state the paragraphs actually read (300.300(c), lines 22-28; 300.34 lines 2 and 21). The CSV was created in this session, so it was corrected in place. sha16 now a3d1ffa82f3e75d6.
artifacts/federal/federal_reviewer_log.md:153: 
artifacts/federal/federal_reviewer_log.md:154: ## UPDATE12 batch 4b (2026-10-22T02:21:05Z / 2026-10-21 19:21 PDT)
artifacts/federal/federal_reviewer_log.md:155: Appended 10 rows (DC-115 to DC-121 and DC-123 to DC-125) to Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE12.csv, now sha16 5d470b433409e05e. New captures: 300.105, .108, .131, .156, .305, .502 (lines 1-13 relied on), .503 (para (a) only), .512, .641; all read in full except where noted. Line-cite key as for batch 4a. Each quote was checked by script against a cited line range; 0 failures (the one flagged string is a keyword search term, not a quote). DC-119 is keyword-only. With DC-100, DC-114 and DC-122 answered earlier, DC-081 to DC-125 are now all answered.
artifacts/federal/federal_reviewer_log.md:156: 
artifacts/federal/federal_reviewer_log.md:157: ## UJ-81/82 counterparts (2026-10-22T02:22:41Z / 2026-10-21 19:22 PDT)
artifacts/federal/federal_reviewer_log.md:158: Created Federal_Counterparts_UT_UJ81-82_2026-10-22.csv (sha16 e7efbc27ac6f5f8a), 2 rows, both PARTIAL. Federal sources: 300.151, .152, .153 and .506, read in full; 300.507(a) for contrast. UT text: reviews/UT/captures/USBE_RulesSpecialEducationReport_captured_20261021T233431Z.layout.txt, lines 4951-5315, which I read in full. Line-cite key: [UT:n] = that layout file at line n (rg/awk numbering, split on newline only); [15x:n] and [506:n] = src/cfr_300.15x_v2.txt and src/cfr_300.506_v2.txt. Each quote was checked against its cited range; 0 failures after two range cites were widened to span wrapped lines. Recorded disagreement, not resolved: IDEA Utah reads IV.F.2 as limiting the parties to the LEA or other public agency and a parent or adult student, but the UT verb is "may include". Note on method: the earlier checks split lines with Python splitlines(); I confirmed it gives the same numbering as split on newline for every DC and federal file cited in UPDATE12, so no earlier line cite shifts.
artifacts/federal/federal_reviewer_log.md:159: 
artifacts/federal/federal_reviewer_log.md:160: ## Append-only record of in-place edits to UPDATE12 (recorded 2026-10-22T02:23:19Z / 2026-10-21 19:23 PDT)
artifacts/federal/federal_reviewer_log.md:161: I edited Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE12.csv in place. The project rule is append-only, and IDA has flagged the edit; this note is the full record. I can recover the original text exactly: the edit was a scripted string replacement, and the old strings below are its literal arguments.
artifacts/federal/federal_reviewer_log.md:162: - When: between the batch 4a append (CSV sha16 b9b01cbc87443cc2, logged 2026-10-22T02:19:51Z) and the next sha16 a3d1ffa82f3e75d6 (logged right after, about 02:20Z / 19:20 PDT). I did not record a separate timestamp for the edit itself.
artifacts/federal/federal_reviewer_log.md:163: - Row DC-109, column federal_counterpart_text_read, segment ORIGINAL: "34 CFR 300.300 (src/cfr_300.300_v2.txt, read in full)". NEW: "34 CFR 300.300 (src/cfr_300.300_v2.txt, para (c) read, lines 22-28; rest of section not read)".
artifacts/federal/federal_reviewer_log.md:164: - Row DC-108, column federal_counterpart_text_read, segment ORIGINAL: "34 CFR 300.34 (src/cfr_300.34_v2.txt, read in full)". NEW: "34 CFR 300.34 (src/cfr_300.34_v2.txt, para (a) line 2 and (c)(5) line 21 read; rest of section keyword-located only)".
artifacts/federal/federal_reviewer_log.md:165: - Reason: the original cells overstated the read. I read only those paragraphs, so "read in full" was not true.
artifacts/federal/federal_reviewer_log.md:166: - The batch 4a sha16 b9b01cbc87443cc2 is the pre-edit file, but I kept no copy of it. All later edits have been and will be appends only.
artifacts/federal/federal_reviewer_log.md:167: 
artifacts/federal/federal_reviewer_log.md:168: ## 300.228 and UJ-60 (2026-10-22T02:24:09Z / 2026-10-21 19:24 PDT)
artifacts/federal/federal_reviewer_log.md:169: Captured 300.228 (HTTP 200, printed, not reserved; read in full). Created Federal_notes_UJ82-300.228_UJ60-300.519_2026-10-22.md (sha16 5a62960fd38acfb6). Quotes checked by script.
artifacts/federal/federal_reviewer_log.md:170: Correction note appended to Federal_notes_UJ82-300.228_UJ60-300.519_2026-10-22.md, sha16 eddd6f2eb3374283 (2026-10-22T02:24:16Z).
artifacts/federal/federal_reviewer_log.md:171: INFERENCE label note appended to Federal_notes_UJ82-300.228_UJ60-300.519_2026-10-22.md, sha16 913598241fa757b6 (2026-10-22T03:13:03Z).
artifacts/federal/federal_reviewer_log.md:172: 
artifacts/federal/federal_reviewer_log.md:173: ## Item 3 leftovers (2026-10-22T03:15:06Z / 2026-10-21 20:15 PDT)
artifacts/federal/federal_reviewer_log.md:174: Created Federal_item3_leftovers_DC_2026-10-22.md (sha16 1f296f451838c4f8). L1 300.208/3025.22 SUPPLIED; L2 300.138/3040.10 PARTIAL (terminology; 300.18 reserved; 'highly qualified' only in App. F index, keyword-only); L3 306(b)/3010.2 PARTIAL and 321(b)/3008.2(d) PARTIAL; L4 622/3031.1(d) PARTIAL plus a lead: 1232g(b)(1)(L) (2013) is not printed in 99.31; L5 300.33 SUPPLIED, with application UNRESOLVED. Script verification 46/46 after the appended note.
artifacts/federal/federal_reviewer_log.md:175: 
artifacts/federal/federal_reviewer_log.md:176: ## DC-232..250 and UP-11 (2026-10-22T03:18:57Z / 2026-10-21 20:18 PDT)
artifacts/federal/federal_reviewer_log.md:177: Created Federal_Counterparts_DC232-250_UP11_2026-10-22.csv (sha16 697e4499fa834552), with 20 rows: PARTIAL 18, NONE FOUND 2 (DC-239 by read and keyword; UP-11 in Part 300 by keyword, and PARTIAL against 42 U.S.C. 675(1)). The quote check passed 85 of 85: each federal quote sits inside its cited line, and each DC or UT quote inside its cited line in S33.ocr.txt, S34.txt, S36.txt or UC_80-3-307. Row source and checker: src/u13/rows.py and src/u13/build.py. New captures: 300.111, .116, .325, .146, .301, .520, .154, .600 (eCFR 2026-10-13, HTTP 200). I read Utah 80-3-307 L34-L262 in full myself.
artifacts/federal/federal_reviewer_log.md:178: - Pin discrepancy in IDEA DC's matrix, recorded and not edited: in S33.ocr.txt, the DC-236 condition sentence ("DCPS is the LEA for District of Columbia resident children ...") is at lines 63-64, not lines 190-208. My DC-232 quote of "enrolled in a public school outside of the District of Columbia" is pinned to scope lines 35-37.
artifacts/federal/federal_reviewer_log.md:179: - Correction for the comparison, recorded and not edited: DC-247 says no CFR counterpart for compensatory education, but 300.151(b)(1) names "compensatory services" (the only hit in Part 300, a keyword result).
artifacts/federal/federal_reviewer_log.md:180: - Limits: I did not re-read the MOA, AI CFSA-15-1 or the Charles H. agreement in full. I checked only the strings I quote against IDEA DC's captured text.
artifacts/federal/federal_reviewer_log.md:181: 
artifacts/federal/federal_reviewer_log.md:182: ## UP-12 and UP-13 (2026-10-22T03:20:24Z / 2026-10-21 20:20 PDT)
artifacts/federal/federal_reviewer_log.md:183: Created Federal_Counterparts_UP12-13_2026-10-22.csv (sha16 79d62428dadd36d6), 2 rows, both PARTIAL. The quote check passed 17 of 17 (src/u13/rows_up.py, build_up.py). I read Utah 80-2a-201 L34-L109 and 80-4-104 L34-L93 in full myself. Federal sections read in full: 300.30, 300.300, 300.519. Keyword searches (keyword-only): "fundamental" (1 hit, unrelated), "liberty" (0 hits), "least restrictive means" (0 hits), "rights of the parent" (2 hits, 300.300(a)(2)(ii)-(iii)). No UP-12 or UP-13 JSON row was on file in reviews/UT/proposed_rows, so these rows are drawn from the captures alone.
artifacts/federal/federal_reviewer_log.md:184: 
artifacts/federal/federal_reviewer_log.md:185: ## NV-L2-109 to 162 (2026-10-22T03:22:30Z / 2026-10-21 20:22 PDT)
artifacts/federal/federal_reviewer_log.md:186: Created Federal_Counterparts_NV-L2-109-162_2026-10-22.csv (sha16 4d087e40b5b2ae33). It has 6 grouped rows, one for each policy cluster (300.01, 300.03, 300.06, 400.06, 500.04, 500.13), and covers all 54 NV rows: PARTIAL 4, NONE FOUND 1 (300.06, keyword), and mixed 1 (400.06). The quote check passed 37 of 37 against the federal captures and the NV texts in NV/jj/sources/L2 (src/u13/rows_nv.py, build_nv.py). I read only the NV lines I cite, not the whole policies. New captures: 300.229 and 300.322 (HTTP 200).
artifacts/federal/federal_reviewer_log.md:187: - Capture-log note: my first two calls passed bare section numbers ("229" and "2"). They returned HTTP 404 and wrote the stub files src/cfr_229_v2.{xml,txt} and src/cfr_2_v2.{xml,txt}, which are logged at 03:20:46Z. The stubs are not sources. I kept them and did not delete them. 300.2 was already on file as cfr_300.2_v2.
artifacts/federal/federal_reviewer_log.md:188: - Focus items: 324(d) and 149(d) reach only youth convicted as adults in adult prisons, so on their face they do not apply to DCFS juvenile facilities (INFERENCE). 323(e)/(f)/(g) and 229(c) bear on 500.04 V.F. Whether Nevada adopted 229(a) or 520(a)(2) is UNRESOLVED. 2(b)(1)(iv) brings the facilities within Part 300. 101(a) is set against the 300.03 V.A.4 education right.
artifacts/federal/federal_reviewer_log.md:189: - GA-14 analogue: per IDEA Nevada's NV-131 row text, NAC 388.283 carries a 30-day term. I have not read it, so that is reported, not verified.
artifacts/federal/federal_reviewer_log.md:190: - Not done this batch: I did not re-read 300.530-536 or 300.322 beyond lines 1-4. Both are marked UNRESOLVED in the rows.
artifacts/federal/federal_reviewer_log.md:191: 
artifacts/federal/federal_reviewer_log.md:192: ## Cases from official sources (2026-10-22T03:24:09Z / 2026-10-21 20:24 PDT)
artifacts/federal/federal_reviewer_log.md:193: Created Federal_Cases_official_2026-10-22.md (sha16 43f29d5f078fd465). It covers Schaffer, Arlington, Endrew F. and Fry, all from supremecourt.gov (bound volumes 546 and 548, plus the 2016-term slip opinions). The quote check passed 7 of 7. LEXIS_QUEUE needs nothing. I read the holding passages in context, not each opinion in full.
artifacts/federal/federal_reviewer_log.md:194: 
artifacts/federal/federal_reviewer_log.md:195: ## NV append A (per-row map) and B (updates) (2026-10-22T03:26:07Z / 2026-10-21 20:26 PDT)
artifacts/federal/federal_reviewer_log.md:196: Appended to Federal_Counterparts_NV-L2-109-162_2026-10-22.csv (sha16 4d087e40b5b2ae33 before, ef2fc8c2346f2339 after). A byte-prefix check confirmed the original content was left unchanged.
artifacts/federal/federal_reviewer_log.md:197: - Append A: one MAP line for each of the 54 rows NV-L2-109..162, giving its group and its federal provision(s), or "no counterpart within group" with the method. New keyword-only searches (Part 300 full): "classification" 0 hits, "corporal" 0, "handbook" 0, "HIPAA" 0, "cognitive" 9 (none on point). Where a line says "no keyword search", the method was a comparison against the group's federal sections.
artifacts/federal/federal_reviewer_log.md:198: - Append B: I read 300.530-300.536 and 300.322 in full (300.531-534 captured this batch, HTTP 200), then wrote 3 update rows. The quote check passed 27 of 27.
artifacts/federal/federal_reviewer_log.md:199:   - NV-L2-122: PARTIAL.
artifacts/federal/federal_reviewer_log.md:200:   - 300.13 rows NV-L2-077, 083, 084: PARTIAL.
artifacts/federal/federal_reviewer_log.md:201:   - NV-L2-160: NONE FOUND, by a full read of 300.322.
artifacts/federal/federal_reviewer_log.md:202:   - NV-L2-161: PARTIAL.
artifacts/federal/federal_reviewer_log.md:203:   - Keyword-only: "confinement", "isolation" and "seclusion" have 0 hits each.
artifacts/federal/federal_reviewer_log.md:204: - NAC 388.283 30-day term: still reported, not verified (IDA is routing it to IDEA Nevada).
artifacts/federal/federal_reviewer_log.md:205: - Standing practice: any later grouped file will carry a per-row map.
artifacts/federal/federal_reviewer_log.md:206: 
artifacts/federal/federal_reviewer_log.md:207: ## 300.168 re-capture and diff (per IDA 03:26) (2026-10-22T03:28:17Z / 2026-10-21 20:28 PDT)
artifacts/federal/federal_reviewer_log.md:208: I re-captured 300.168 from eCFR (versioner 2026-10-13, HTTP 200) as src/cfr_300.168_v2.txt (sha16 59ce1b42a465b1ab). The earlier file is src/cfr_300.168.txt (sha16 cd4f40cb9ace3d88), left in place and not edited.
artifacts/federal/federal_reviewer_log.md:209: - Diff result: after removing blank lines and leading spaces, the two files are identical. The only difference is a missing final newline in v2.
artifacts/federal/federal_reviewer_log.md:210: - Line 6 of the old file reads in full: "... involved in, or concerned with the education of children with disabilities, including—". It is not truncated. The em dash belongs to the source text, and items (1)-(11) follow on lines 8-28.
artifacts/federal/federal_reviewer_log.md:211: - IDEA Georgia's lead (GA-82: "line 6 ends 'education of children with'") does not match the file as read. Recorded here, not resolved. A possible cause is display-width cutting (INFERENCE, unverified).
artifacts/federal/federal_reviewer_log.md:212: - The federal text is not Governor-only. It reads "appointed by the Governor, or any other official authorized under State law to make such appointments" (v2 line 2; 20 U.S.C. 1412(a)(21)(B), usc1412.txt line 325).
artifacts/federal/federal_reviewer_log.md:213: 
artifacts/federal/federal_reviewer_log.md:214: ## GA-82 to GA-85 counterparts (2026-10-22T03:28:17Z / 2026-10-21 20:28 PDT)
artifacts/federal/federal_reviewer_log.md:215: New file: Federal_Counterparts_GA-82-85_2026-10-22.csv (sha16 f010dbb3d9953c50). The quote check passed 33 of 33.
artifacts/federal/federal_reviewer_log.md:216: - Sources I read myself:
artifacts/federal/federal_reviewer_log.md:217:   - the GA 160-4-7 capture, lines 81-128 and 3294-3345;
artifacts/federal/federal_reviewer_log.md:218:   - the DJJ manual: I re-ran pdftotext -layout on the PDF (sha16 86d8953096ba076f, which matches) and read lines 585-616 and 3430-3490. A copy of that text is at src/u13/djjman_pdftotext-layout.txt.
artifacts/federal/federal_reviewer_log.md:219: - Statuses:
artifacts/federal/federal_reviewer_log.md:220:   - GA-82: SUPPLIED for seats (10) and (11); appointing authority UNRESOLVED.
artifacts/federal/federal_reviewer_log.md:221:   - GA-83: PARTIAL. GA omits the 1974 split, the "prior to adjudication" condition and the 99.38 certification. Keyword re-run for "99.38" and "November": 0 hits.
artifacts/federal/federal_reviewer_log.md:222:   - GA-84: PARTIAL. GA runs a 3-day clock from enrollment against the federal 30-day SEA frame from the determination. A new item: the "short-term or temporary" foster parent surrogate ground has no counterpart in 519(a); it is compared with 300.30(a)(2).
artifacts/federal/federal_reviewer_log.md:223:   - GA-85: SUPPLIED on its face. INFERENCE: a DFCS caseworker falls within 519(d)(2)(i). Application to judge-appointed surrogates is UNRESOLVED.
artifacts/federal/federal_reviewer_log.md:224: - Per-row map appended.
artifacts/federal/federal_reviewer_log.md:225: - 2026-10-22T03:29:40Z (2026-10-21 20:29 PDT): wrote Federal_Schaffer_burden_leads_2026-10-22.md (sha16 e06903857ccd3295); item (3) Schaffer leads, 4 states; correction C-1 appended (pins).
artifacts/federal/federal_reviewer_log.md:226: - 2026-10-22T03:29:54Z: Schaffer leads file: all 15 state-line quotes script-verified against reviewer captures (GA 5084-5089, NV 388.467 L1, DC 38-2571.03 L43-45, 5-A 3053.6 L35-39, UT Uintah L57-65, Provo L294-296).
artifacts/federal/federal_reviewer_log.md:227: - 2026-10-22T03:31:15Z (2026-10-21 20:31 PDT): wrote Federal_672_agreement_facts_2026-10-22.md (sha16 e9dff1ce704a559a): item (4) 672 agreement facts; 14/14 quotes verified after C-1.
artifacts/federal/federal_reviewer_log.md:228: - 2026-10-22T03:31:23Z (2026-10-21 20:31 PDT): 672 file C-2 appended (sha16 b32447c8bc550156).
artifacts/federal/federal_reviewer_log.md:229: 
artifacts/federal/federal_reviewer_log.md:230: ## 2026-10-22T03:33:52Z (2026-10-21 20:33 PDT) IDA 03:30 items (a)-(c)
artifacts/federal/federal_reviewer_log.md:231: - (a) Federal_Counterparts_UP14-15_2026-10-22.csv (sha16 b4f9b0a1963b9661): UP-14 PARTIAL (300.101(a), 300.323(e)-(f), 675(1)(G)); UP-15 SUPPLIED on its face, scope UNRESOLVED; 13/13 quotes verified; per-row map appended.
artifacts/federal/federal_reviewer_log.md:232: - (b) Federal_NAC388.283_vs_300.519h_2026-10-22.md (sha16 1d76086238447e74): same 30-day clock; actor differs (public agency vs SEA), appointment vs assignment, trigger wording differs.
artifacts/federal/federal_reviewer_log.md:233: - (c) Federal_Counterparts_NV-L2-163-185_2026-10-22.csv (sha16 30d3e5531826347c): 3 groups (500.17 PARTIAL/NONE FOUND; 500.18 PARTIAL/NONE FOUND; 500.19 NONE FOUND keyword-only); 23/23 quotes verified; 23-row per-row map appended.
artifacts/federal/federal_reviewer_log.md:234: - New captures (eCFR, HTTP 200): 300.302, 300.610, 300.611, 300.623.
artifacts/federal/federal_reviewer_log.md:235: - Builder: src/u13/build_any.py with rows_up1415.py, rows_nv163.py.
artifacts/federal/federal_reviewer_log.md:236: 
artifacts/federal/federal_reviewer_log.md:237: ## 2026-10-22T03:37:12Z (2026-10-21 20:37 PDT) IDA 03:34 items (1)-(3)
artifacts/federal/federal_reviewer_log.md:238: - (1)+(2) Federal_Counterparts_GA-89_GA-48burden_2026-10-22.csv (sha16 b2729b6736789cc8): GA-89 PARTIAL (DJJ fifth surrogate ground, short-term or temporary foster assignment, has no 300.519(a) counterpart; 300.30(a)(2) "unless" route; GA rule .11 lists only the four federal grounds; GA definition (31) omits the "unless" clause); GA-48 burden item PARTIAL vs Schaffer, 546 U.S. at 61-62. 17/17 quotes verified; map appended.
artifacts/federal/federal_reviewer_log.md:239: - (3) Federal_Counterparts_NV-L2-186-204_2026-10-22.csv (sha16 8d203688f48a0b0b): 600.02 NONE FOUND (keyword); CCJJS PARTIAL 193/194/196/198; Washoe PARTIAL 202/203/204. 34/34 quotes verified; 19-row map appended.
artifacts/federal/federal_reviewer_log.md:240: - Builder src/u13/build_any.py (keys added: 546bv, N6002, CC, WA); rows_ga89.py, rows_nv186.py.
artifacts/federal/federal_reviewer_log.md:241: 
artifacts/federal/federal_reviewer_log.md:242: ## 2026-10-22T03:38:37Z (2026-10-21 20:38 PDT) IDA 03:35 PA items
artifacts/federal/federal_reviewer_log.md:243: - (1) Federal_Counterparts_DC232-250_UP11_2026-10-22.csv: appended C-1 (DC-242 plural phrases at 324 line 32, singular at line 35). sha16 697e4499fa834552 -> 2a99ed57168c3bda.
artifacts/federal/federal_reviewer_log.md:244: - (2) Same file: appended N-1 checker note. New widened checker src/u13/check_csv.py (every cell; pin before or after). Before the appends: 86 verified, 0 failed, 30 unpinned. PA count 87 not reconciled. Today's four new files re-run: 13/23/17/34 verified, 0 failed.
artifacts/federal/federal_reviewer_log.md:245: - (3) CFR_CAPTURE_LOG_GA39_56.txt: appended full URL, HTTP 200 and full sha256 for 546bv.pdf and 548bv.pdf. A re-fetch matched the stored bytes.
artifacts/federal/federal_reviewer_log.md:246: - GA-89, GA-48 and NV 186-204 were already done at 03:37Z (see the entry above).
artifacts/federal/federal_reviewer_log.md:247: 
artifacts/federal/federal_reviewer_log.md:248: ## 2026-10-22T03:40:38Z (2026-10-21 20:40 PDT) IDA 03:38 item (B)
artifacts/federal/federal_reviewer_log.md:249: - Federal_Counterparts_UP16-20_2026-10-22.csv (sha16 da901b9c6da26df4): UP-16 PARTIAL; UP-17 SUPPLIED on its face vs 675(1)(G)(i); UP-18 PARTIAL (675(1)(B) not read); UP-19 SUPPLIED with one item PARTIAL (best-interest factors, transportation-cost rule and dispute rule not found in 6311/6312 as read; ED/HHS 2016 guidance not captured); UP-20 PARTIAL. ESSA is labeled a related federal baseline. Builder checker 56/56; widened checker run; map appended. ESSA was already captured from govinfo (CAPTURE_LOG lines 9-10). Item (A) was done at 03:38:37Z.
artifacts/federal/federal_reviewer_log.md:250: 
artifacts/federal/federal_reviewer_log.md:251: - 2026-10-22 03:44 UTC (20:44 PDT): UP-18 U-1 appended to Federal_Counterparts_UP16-20 (HR4980 link KEPT; H.R. 4980 = Pub. L. 113-183 per govinfo PLAW header line 9; rights document is 42 U.S.C. 675a(b)(1)-(2), added by sec. 113(d), not 675(1)(B); 675a and PLAW-113publ183 captured from govinfo 03:41:16Z, HTTP 200). UP-19 U-1 appended: ED/HHS NRG June 23 2016 captured from acf.hhs.gov (redirect to acf.gov), sha256 a674eb14...eb6d, 28 pp, AGENCY GUIDANCE, NOT LAW; Q12 factors, line 530 transportation costs, lines 872-873 disputes match the flyer; ed.gov copies HTTP 403. File now 74 verified, 0 failed, 9 unpinned; sha16 4405d26f939ba7a6. New file Federal_Counterparts_GA-90-91_2026-10-22.csv (sha16 cc240f4d42470028): GA-90 NONE FOUND for an IDEA interagency team (method stated; Part 303 not searched), PARTIAL on LEA seat vs 300.321; GA-91 PARTIAL vs 300.111/300.301. 23/23 quotes verified at build; map present.
artifacts/federal/federal_reviewer_log.md:252: - 2026-10-22 03:44 UTC: correction to the entry above: the map rows were appended after the build (the builder does not write G); Federal_Counterparts_GA-90-91_2026-10-22.csv now sha16 fbc8f78d7ae9acba, 3 MAP rows.
artifacts/federal/federal_reviewer_log.md:253: - 2026-10-22T03:46:22Z (2026-10-21 20:46 PDT): Schaffer leads C-1 (UT burden search command recorded, undue-burden statement withdrawn, Title 80 hits listed, UT statement stays UNRESOLVED) and C-2 (Provo quote L294-296, not L104) appended; capture-log note for row 19 (300.168 .txt sha256 cd4f40cb...a172) appended.
artifacts/federal/federal_reviewer_log.md:254: - 2026-10-22 03:50 UTC (20:50 PDT): GA-90 U-1 appended (Part 303 captured from eCFR 03:47:05Z, 5087 lines; NONE FOUND for a local team; 303.600 State ICC is a different body); GA-90-91 file sha16 80df7988f4c39aa7, 28 verified. New Federal_Counterparts_GA-92-94_UP21-22_2026-10-22.csv (sha16 0e71c3dd595a2015): GA-92 PARTIAL vs 300.30(a)(3), (b)(2); GA-93 PARTIAL vs 300.323(e), (g), ESSA 6311(g)(1)(E) related baseline; GA-94 PARTIAL vs 300.613-.625, 99.31(a), (a)(9), 1232g(b)(1)(L) and (b)(2)(B) (99.31 has no caseworker or dependency text, keyword-only); UP-21 NONE FOUND (method stated), related 300.39(b)(1), 300.17(a); UP-22 PARTIAL vs 1232g(b)(1)(L), 99.31(a)(5)/99.38, (a)(9), 300.622(a). New eCFR captures: 300.17, .39, .613-.621, .624, .625.
artifacts/federal/federal_reviewer_log.md:255: - 2026-10-22 03:51 UTC (20:51 PDT): UP16-20 C-2 appended (APA ellipsis corrections for truncated quotes in UP-18 U-1 and UP-19 U-1, incl. [675a:29], [675:14], [PL183:603], [NRG16:530]; P300 col 5 split re-pinned to 1018-1019). Checker v2 (ellipsis-aware); trunc_scan.py added. Federal_Counterparts_UP16-20_2026-10-22.csv sha16 01d6427192f783e2. Queued: truncation scan of all earlier 2026-10-22 files.
artifacts/federal/federal_reviewer_log.md:256: - 2026-10-22T03:56:18Z (2026-10-21 20:56 PDT): IDA 03:53 items.
artifacts/federal/federal_reviewer_log.md:257:   - (1) Checker v3 (src/u13/check_csv.py) reads the pin list from the project copy src/u13/build_any.py and pairs pins across "(" or ")". v1 is kept as src/u13/check_csv_v1.py.
artifacts/federal/federal_reviewer_log.md:258:   - Keys appended to build_any.py (project and /tmp copies identical): UT, UT201, UT104 (from build_up.py and the UJ81-82 source), plus 672, 1355, GA248, NV501, UT512.
artifacts/federal/federal_reviewer_log.md:259:   - DC232-250: N-2 appended (sha16 8d1f57bf8512e2f2). The counts reconcile: the body gives 86 under v1 and 87 under v3 (DC-236 [33:2] now paired, matching the PA's 87); C-1 adds 2, for 89. The checker now reads 90 because N-2 quotes the DC-236 phrase.
artifacts/federal/federal_reviewer_log.md:260:   - UP12-13: the 5 failures were caused by missing keys UT201 and UT104. Now 17 verified, 0 failed.
artifacts/federal/federal_reviewer_log.md:261:   - UT_UJ81-82: the 18 failures were caused by the missing UT key. 1 real pin error remains: UJ-82 "State complaint" [UT:5293] should be [UT:5293-5294]. C-1 appended (sha16 f1f6737408ef6496). The checker now reads 2 failed, because C-1 quotes the wrong pin.
artifacts/federal/federal_reviewer_log.md:262:   - The UJ81-82 and UP12-13 files lack per-row map rows. Open.
artifacts/federal/federal_reviewer_log.md:263:   - (3) 672 file: C-3 appended. The recount gives 16 pinned source quotes in the body, all verified; the PA is right and my 14 was wrong. The NV 316-317 ellipsis is replaced by the joined form.
artifacts/federal/federal_reviewer_log.md:264:   - (4) A-1 appended: NV/welfare/sources/L2_NDE_ESSA_AB491.txt L96-110 (NDE slides, Aug 18 2017). They describe a WCSD-WCDSS MOU with "Transportation to School of Origin to be funded through Title IV-E (2017)" [103]. The federal hook is 675(4)(A) [675:38]. This does not change "no CW-JJ IV-E agreement captured" (INFERENCE: an education to child welfare transport MOU). The MOU text is not captured. 672 file sha16 dd6b97abc8bc6a40.
artifacts/federal/federal_reviewer_log.md:265:   - sha256 for the 675a and PL183 .htm/.txt captures appended to src/usc/CAPTURE_LOG.txt.
artifacts/federal/federal_reviewer_log.md:266: - 2026-10-22T03:56:53Z (2026-10-21 20:56 PDT): trunc_scan run over all 12 Federal_Counterparts_*2026-10-22.csv. Raw output in TRUNC_SCAN_raw_20261022T035653Z.txt; a mechanical filter dropping list-item ends (; and / ; or / dash / colon / comma) and next-is-punctuation leaves the flags in TRUNC_SCAN_review_20261022T035653Z.txt. Not yet reviewed by reading; a flag is not a finding (a phrase quote may end mid-sentence under APA 7). Row-by-row review open.
artifacts/federal/federal_reviewer_log.md:267: - 2026-10-22T04:01:14Z (2026-10-21 21:01 PDT): IDA 03:58 items.
artifacts/federal/federal_reviewer_log.md:268:   - Per-row maps appended: UJ81-82 (UJ-81 IV.E with 300.151-.153; UJ-82 IV.F with 300.506) and UP12-13 (UP-12, UP-13 with 300.30, .300, .519, plus "no counterpart within group" items and the method). Maps were appended before the M-1 notes.
artifacts/federal/federal_reviewer_log.md:269:   - Meaning-test scan. This replaces the end-truncation scan logged earlier; TRUNC_SCAN_* files are superseded and kept.
artifacts/federal/federal_reviewer_log.md:270:     - Tool: src/u13/meaning_scan.py.
artifacts/federal/federal_reviewer_log.md:271:     - Scope: the 18 Federal files dated 2026-10-22 (12 CSV, 6 MD).
artifacts/federal/federal_reviewer_log.md:272:     - Method: for each pinned quote that verifies, take the omitted text in the same clause before and after it (clause bounded by ". ", ";" or a subparagraph marker). Flag it when that text holds a negation, condition, exception or qualifier term and the qualifier is not already carried in the same cell.
artifacts/federal/federal_reviewer_log.md:273:     - Results: 510 quotes scanned; 131 machine candidates (MEANING_SCAN_candidates_20261022.txt), all read by me.
artifacts/federal/federal_reviewer_log.md:274:     - 21 quote instances in 16 row items have an omitted qualifier that bears on the comparison. 1 of them, DC-248, is possible (the clause it attaches to is UNRESOLVED).
artifacts/federal/federal_reviewer_log.md:275:     - Corrections appended as "MEANING NOTE M-1 (<row>)" in 7 files:
artifacts/federal/federal_reviewer_log.md:276:       - DC232-250: DC-237, -241, -248, -249.
artifacts/federal/federal_reviewer_log.md:277:       - GA-92-94: GA-93, GA-94.
artifacts/federal/federal_reviewer_log.md:278:       - NV-L2-109-162: NV-L2-129, -138, -077/083/084.
artifacts/federal/federal_reviewer_log.md:279:       - NV-L2-186-204: NV-L2-186, -199.
artifacts/federal/federal_reviewer_log.md:280:       - UP12-13: UP-13.
artifacts/federal/federal_reviewer_log.md:281:       - UP14-15: UP-15.
artifacts/federal/federal_reviewer_log.md:282:       - UJ81-82: UJ-81.
artifacts/federal/federal_reviewer_log.md:283:     - Every new quote in M-1 verifies (checker v3).
artifacts/federal/federal_reviewer_log.md:284:     - Limits: keyword-based triggers, so a qualifier phrased without a listed term is not caught. Unpinned quotes are not scanned. Older (pre-10-22) files are not scanned.
artifacts/federal/federal_reviewer_log.md:285:     - No ellipses were added in bulk.
artifacts/federal/federal_reviewer_log.md:286: 
artifacts/federal/federal_reviewer_log.md:287: - 2026-10-22T04:12Z (21:12 PDT): TRUNC_SCAN_review_20261022T035653Z.txt reinstated per IDA 03:59 (supersede label withdrawn). Adjudication A-1 plus addendum appended: 222 lines, one per flag, read one by one against source and cell. CORRECT 25 (19 already handled in M-1; 6 new: #1 DC-238, #78 GA-94, #83 UP-22, #141/#142 NV-L2-192 to 198, #185 UP-20), KEEP 197. New notes: M-2 (DC-238, GA-94, UP-22, NV-L2-192 to 198, UP-20). M-2 rows in DC, GA-92-94 and NV-186-204 were written with doubled quote marks; restated as M-2a (append-only). NV M-2a pin [CC:672] wrong; M-2b gives [CC:673]. Checker v3: DC 99/0/41, GA-92-94 62/0/14, NV-186-204 38/1/7 (the 1 is the M-2a wrong pin, left in place), UP16-20 86/0/11. Schaffer leads C-2: PA Title 80 list cross-checked, no missing hit; L1475-1483 section resolved as 80-6-504 (OBSERVED, XML attributes).
artifacts/federal/federal_reviewer_log.md:288: 
artifacts/federal/federal_reviewer_log.md:289: - 2026-10-22T04:08:33Z (2026-10-21 21:08 PDT): IDA 04:03 items.
artifacts/federal/federal_reviewer_log.md:290:   - Timestamp correction: my entries stamped 04:12Z (this log and status.md) were written at or before 04:05:40Z and 04:05:43Z (ls). The 04:06Z to 04:12Z stamps in the M-2, M-2a, M-2b and A-1 rows and in Schaffer C-2 were typed by hand ahead of the write, not read from date -u. Each file now has an appended correction giving the observed write time. From now on every stamp comes from date -u at write time.
artifacts/federal/federal_reviewer_log.md:291:   - PA meaning flags (part 120): MEANING NOTE M-3 rows for UP-16 [P300:3745-3746] 'appropriate.', UP-19 [FLY:55-56] best-interest condition, and UP-22 field 6 [1232gs:157] 'provided that ... will not be disclosed' proviso. A GA-93 M-3 confirms M-1's best-interest conditions cover fields 6 and 7. GA-94 item 7 is covered by M-2/M-2a. Truncation review #82 changed to CORRECT (addendum 2): CORRECT 26, KEEP 196.
artifacts/federal/federal_reviewer_log.md:292:   - UP16-20 C-3: C-2's 'col 5' means the 7th CSV field. C-2's 03:53Z stamp is hand-typed; written by 03:52:40Z per IDA. The 'v2 03:53Z' and 'v3 03:55Z' labels in check_csv.py are hand-typed too.
artifacts/federal/federal_reviewer_log.md:293:   - src/u13 is now self-contained. Every '/tmp/u13' reference is replaced with the script's own directory. The DJJ path now points to src/u13/djjman_pdftotext-layout.txt, which is byte-identical to /tmp/u13/djjman.txt (cmp, sha256 44d4f1da...e608). rows_tmp_GA.py and rows_tmp_UT.py are copied in. I tested with /tmp/u13 renamed: check_csv.py on all 12 files gives the same counts, and trunc_scan.py, meaning_scan.py and check_csv_v1.py run. The build_*.py scripts were patched and syntax-checked but not re-run, so the counterpart files are not regenerated.
artifacts/federal/federal_reviewer_log.md:294: - 2026-10-22T04:14:18Z (2026-10-21 21:14 PDT): IDA 04:06 and 04:08 items.
artifacts/federal/federal_reviewer_log.md:295:   - PA MEANING FLAG cross-references (audit/08 part 120): (1) UP-16 [P300:3745] covered by M-3 (UP-16). (2) UP-19 [FLY:55-56] covered by M-3 (UP-19); the same condition governs [FLY:57] and [FLY:58]. (3)-(5) GA-93 covered by M-1 (GA-93) with the M-3 (GA-93) scope note (fields 6 and 7). (6) UP-22 field 6 proviso covered by M-3 (UP-22). (7) GA-94 covered by M-2/M-2a (GA-94).
artifacts/federal/federal_reviewer_log.md:296:   - New M-3 rows: UP-16 675G ([675G:35] condition, KEEP on candidate #96 reversed), stamp 04:11:30Z; DC-243 ([102:2] exception lead-in), 04:11:30Z; DC-240 ([321:15] consent and "to the extent appropriate"), 04:13:47Z; NV-L2-122 ([536:2] change-of-placement lead-in), 04:13:47Z.
artifacts/federal/federal_reviewer_log.md:297:   - MEANING_SCAN_adjudication_20261022T041158Z.txt (companion to the 131-line candidate file): CORRECT 32, KEEP 99; per-instance M-1 list (22 lines in 14 notes / 16 row items; the 04:01Z "21 instances" count is not reconciled, the list governs); meaning_scan v2 results and limits.
artifacts/federal/federal_reviewer_log.md:298:   - meaning_scan v2: triggers added; v1 multi-word coverage defect found and fixed; 37 new candidates (3 read, 34 OPEN), 26 note-row lines.
artifacts/federal/federal_reviewer_log.md:299:   - Timestamp corrections (C-2/C-3/C-4) and the /tmp/u13 dependency closure were done earlier (04:04-04:08Z).
artifacts/federal/federal_reviewer_log.md:300: - 2026-10-22T04:15:39Z (2026-10-21 21:15 PDT): IDA 04:13 items (2)-(5): Schaffer C-4 (XML labels one subsection ahead; corrected to (8) L1475, (9)(a) L1476, (9)(b) L1480, (10)(b)(i) L1483); UP16-20 C-5 (M-3 'raw scan' claim wrong, UP-16 absent from raw scan, cause UNRESOLVED; C-3 write time is 03:51:57 per PA); TRUNC review addendum 3 (#61 reason). Item (1) was delivered at 04:14Z before this message arrived.
artifacts/federal/federal_reviewer_log.md:301: - 2026-10-22T04:17:32Z (2026-10-21 21:17 PDT): IDA 04:15 item 2: meaning_scan v3 (5 trigger phrases added); 34 OPEN v2 lines and 9 v3 lines marked in adjudication Addendum 3 (+correction to v2 #2 reason); M-3 (DC-242) appended at 04:17:17Z ((d)(2)(ii) exemption [324:36]). DC checker 106/0/45. Next: item 3 NV-L2-205 to 219.
artifacts/federal/federal_reviewer_log.md:302: 
artifacts/federal/federal_reviewer_log.md:303: ## 2026-10-22T04:23:31Z (2026-10-21 21:23 PDT) NV-L2-205 to 223 counterparts
artifacts/federal/federal_reviewer_log.md:304: Federal_Counterparts_NV-L2-205-223_2026-10-22.csv: 4 groups (205-208 WEDP, 209-213 WNJR, 214-219 FY26 MOU, 220-223 2017 Protocol), per-row map for all 19 rows, 3 M-3 notes. Checker v3: verified 92 failed 0 unpinned 0. Meaning scan v3: 24 flags; 10 conditions added in M-3 notes, 14 KEEP (sequential clauses, lead-ins already restated, purpose clauses, false positives on "appropriate"). New keys in build_any.py: WEDP, WNJR, MOU, NRG24, P300F, MOU17 (pre-edit copy /tmp/build_any_pre205.py). Open: actor of NV-L2-216 (OCR headings illegible; 2017 parallel structure points to WCSD, INFERENCE; image not read); 99.31 capture has no child welfare exception (keyword-only); IV-E admin cost rule (45 CFR 1356.60) and ACYF-CB-PI-10-11 not captured; MOU 50% WCSD match vs NRG24 F-16 non-Federal portion statement UNRESOLVED, no finding.
artifacts/federal/federal_reviewer_log.md:305: 
artifacts/federal/federal_reviewer_log.md:306: ## 2026-10-22T04:31:27Z (2026-10-21 21:31 PDT) DC-251 to 261 federal counterparts
artifacts/federal/federal_reviewer_log.md:307: - File: Federal_Counterparts_DC-251-261_2026-10-22.csv (30 rows: 11 counterpart rows, map header plus 11 map rows, 5 M-3 notes, 1 M-3a note). Source: src/u13/rows_dc251.py. Keys added to build_any.py: S40, S41, S42, S43, DCL14, 1414s (backup /tmp/build_any_pre251.py).
artifacts/federal/federal_reviewer_log.md:308: - Sources read: S40 in full; S41 1-841 in full; S42 in full; S43 1-68 in full, attached base MOA keyword-checked. Federal: 300.17, 300.2, 300.33, 300.34(a), 300.43(a), 300.101, 300.102, 300.105, 300.111, 300.149, 300.151(b), 300.154, 300.300(b), 300.321(a), 300.323(c)-(d), 300.324(d), 300.502(a)-(b), 300.520, 300.613, 300.623; 20 USC 1412(a)(11), 1414(d)(1)(B); OSEP DCL 2014-12-05 lines 196-242 (agency guidance, not law).
artifacts/federal/federal_reviewer_log.md:309: - Checker v3: verified 163 failed 0 unpinned 2 (the 2 are the OCR tokens Ifa and |.11 in the M-3 note; pinned in the M-3a row, append-only). Meaning scan v3: 38 flags (/tmp/mt/dc251_scan.txt); 12 conditions added in the M-3 notes; 26 KEEP. sha16 3ebefc3cc160da6f.
artifacts/federal/federal_reviewer_log.md:310: - Open: Letter to Yudien (2003) NOT CAPTURED; child find reach of 300.102(a)(2)(i) UNRESOLVED; whether D.C. Jail is an adult prison for 300.324(d) UNRESOLVED; whether a session refusal is a 300.300(b)(4) revocation UNRESOLVED; 5A DCMR 3001.4, 5E DCMR 3002.2(a), D.C. Code 38-2573.01 and Charles H. para. 106 not read by me; S42 OCR date 2028 not resolved.
artifacts/federal/federal_reviewer_log.md:311: 
artifacts/federal/federal_reviewer_log.md:312: - 2026-10-22T04:33:47Z (2026-10-21 21:33 PDT): IDA 04:31 and 04:32 items.
artifacts/federal/federal_reviewer_log.md:313:   - MEANING_SCAN_adjudication Addendum 4 appended (sha16 3fe00cf9e60f5b6a): A-1 19 reconciled to the M-1 list of 22 (GA-93 [6311:451] trunc #66, DC-237 [S33:210-228], DC-241 [S34:82-83]); #21 reason restated, KEEP stands; UP-16 raw-scan miss: cause NOT DETERMINED, 03:56 scanner state not preserved.
artifacts/federal/federal_reviewer_log.md:314:   - DC-251-261 NOTE M-4 appended (04:32:04Z): DC-255 and DC-256 restated as SUPPLIED (cited text matches); MATCH withdrawn as a status. Checker 163/0/2 unchanged. sha16 a364e5ea429cc604.
artifacts/federal/federal_reviewer_log.md:315:   - build_any backups moved to src/u13/backups/ (build_any_pre205.py sha256 41f7549e...ca513d23; build_any_pre251.py f821f474...7caae47f); hashes in BACKUPS_sha256.txt.
artifacts/federal/federal_reviewer_log.md:316:   - Capture queue: 45 CFR 1356.60, ACYF-CB-PI-10-11, then Letter to Yudien (ed.gov), then DC-262 to 272.
artifacts/federal/federal_reviewer_log.md:317: 
artifacts/federal/federal_reviewer_log.md:318: ## 2026-10-22T04:39:47Z (2026-10-21 21:39 PDT) DC-262 to 272 (S47, DOC PP 4110.7G, agency policy, not law)
artifacts/federal/federal_reviewer_log.md:319: - Output: Federal_Counterparts_DC-262-272_2026-10-22.csv, 11 rows, per-row map (11 MAP rows), NOTE M-1 to M-3. sha16 92e766be560c4016.
artifacts/federal/federal_reviewer_log.md:320: - Build ok 174 bad 0 (one BADpre on DC-267 [S47:617] fixed by re-splitting the quote at the line break before output). Checker v3: verified 190, failed 0, unpinned 4 (three short terms and one paraphrase reference; M-3 pins the terms and corrects the M-1 misquote of my own paraphrase).
artifacts/federal/federal_reviewer_log.md:321: - Meaning scan v3: 46 flags; conditions added in M-1 (DC-266, 267, 268, 270, 271, 272). Trunc scan run; END-TRUNC flags are line-break splits of quotes continued in the next pin.
artifacts/federal/federal_reviewer_log.md:322: - Inputs: DC matrix 288 lines sha16 779552bfad26725a (read, not edited); S47 sha16 e5383d182328eb52 read in full. build_any.py backed up to src/u13/backups/build_any_pre262.py (sha256 appended to BACKUPS_sha256.txt) before adding P key S47.
artifacts/federal/federal_reviewer_log.md:323: - UNRESOLVED: 5A DCMR 3001.4; provider records policy; Consent to Provide Special Education Services form; Letter to Yudien (403); whether D.C. Jail is an adult prison; persons under 18 in DOC.
artifacts/federal/federal_reviewer_log.md:324: - Captures CAP-1450 (45 CFR 1356.60) and CAP-PI1011 (ACYF-CB-PI-10-11) and CAP-YUD (not captured) are recorded in src/CAPTURE_LOG_guidance.txt at 04:35:11Z; noted here for the log.
artifacts/federal/federal_reviewer_log.md:325: - Queue: DC-273 to 279 (S48-S50); awaiting-Federal DC rows; then UT UP-23 to 44 less UP-35 with the 300.30(a)(2) foster-parent item (IDA 04:40).
artifacts/federal/federal_reviewer_log.md:326: 
artifacts/federal/federal_reviewer_log.md:327: ## 2026-10-22T04:42:38Z (2026-10-21 21:42 PDT) Point (c), NRG24 host match, Letter to Yudien (IDA 04:36, 04:40)
artifacts/federal/federal_reviewer_log.md:328: - Order note: IDA 04:36 asked for point (c) before DC-262; DC-262 to 272 was already finished at 04:39Z, before I read that message. Point (c) was done next. The IDA 04:17 message arrived late; its items (scan, NV-205-219, DC-251-260) were already done.
artifacts/federal/federal_reviewer_log.md:329: - Point (c): NOTE appended to Federal_Counterparts_NV-L2-205-223_2026-10-22.csv, followed by a pin CORRECTION row (four pins were off by one to three lines; append-only, so the checker reports 116 verified and 4 failed, and the 4 failures are the superseded pins). sha16 31cd88903b1f4d85. P keys PI1011, E1356 and YUD were added to build_any.py after a backup to src/u13/backups/build_any_pre_pointc.py.
artifacts/federal/federal_reviewer_log.md:330: - NRG24: browser PDF sha256 matches the PDF on file; host match CONFIRMED and FLAG cleared in CAPTURE_LOG_guidance (sha16 a79683ae5188a61b).
artifacts/federal/federal_reviewer_log.md:331: - Yudien: logged; PDF text extracted and read in full; the page file is labeled RENDERED DOM. The text layer date reads 2008 and the host says 2003 (logged). NOTE Y-1 was appended to the DC-251-261 file (170/0/2, sha16 34a381d405196ea8) and to the DC-262-272 file (201/0/4, sha16 2b787987e3188fd4). The DC-253 child find point is NARROWED to a question of DC law (5A DCMR 3001.4, not read), not resolved.
artifacts/federal/federal_reviewer_log.md:332: 
artifacts/federal/federal_reviewer_log.md:333: ## 2026-10-22T04:44:19Z (2026-10-21 21:44 PDT) IDA 04:41 and 04:43 items
artifacts/federal/federal_reviewer_log.md:334: - 04:41 items (1) point (c) and (2) Yudien/DC-253 were already done at 04:42Z (see entry above).
artifacts/federal/federal_reviewer_log.md:335: - 2 CFR 200.306 captured (one empty 302 try kept as a record), read in full, and appended to point (c) item (2) in the NV-205-223 file: 127 verified, 4 failed (the superseded pins), sha16 484615f56eedb305. P key C200306 added after a backup to u13/backups/build_any_pre200306.py.
artifacts/federal/federal_reviewer_log.md:336: - Yudien page 1 rendered; IMAGE READING AUG 19 2003 logged in CAPTURE_LOG_guidance and replaces the earlier inference.
artifacts/federal/federal_reviewer_log.md:337: 
artifacts/federal/federal_reviewer_log.md:338: ## 2026-10-22T04:46:49Z (2026-10-21 21:46 PDT) DC-273 to 279 (S48, S49, S50)
artifacts/federal/federal_reviewer_log.md:339: - S48 (368 lines), S49 (433), S50 (63) read in full by me. sha16 S48 2296c3303ea00405, S49 8ea4289fee6e3df4, S50 2035b8c226e94228. All agency form, not law.
artifacts/federal/federal_reviewer_log.md:340: - build_any.py backed up to u13/backups/build_any_pre273.py (hash appended); P keys S48, S49, S50 added.
artifacts/federal/federal_reviewer_log.md:341: - Federal_Counterparts_DC-273-279_2026-10-22.csv: 7 rows (273 NONE FOUND; 275 NONE FOUND within Part 300 with RELATED FEDERAL BASELINE 6311(g)(1)(E), 6312(c)(5)(B); 274, 276, 277, 278, 279 PARTIAL), 7-row map, NOTE K-1 (keyword counts), NOTE M-1 (conditions). Check 89/0/3, sha16 b94aeba0a4d2c98f.
artifacts/federal/federal_reviewer_log.md:342: - UNRESOLVED: back of S50 not captured; whether CFSA is a public agency for 300.301(b); whether MDT is the IEP Team.
artifacts/federal/federal_reviewer_log.md:343: - Queued from IDA 04:45: 2 CFR part 300 and 45 CFR 75.306 capture, after UT UP-23 to 44.
artifacts/federal/federal_reviewer_log.md:344: 
artifacts/federal/federal_reviewer_log.md:345: ## 2026-10-22T04:49:58Z (2026-10-21 21:49 PDT) Awaiting-Federal DC rows, batch 1 (DC-114, DC-126 to 133)
artifacts/federal/federal_reviewer_log.md:346: - Scope check: status.md line 184 lists 179 rows; 72 covered in my files (DC-098 to 125 except 114; DC-232 to 279); 107 missing (DC-114, DC-126 to 231). Earlier estimate DC-145 to 191 was wrong.
artifacts/federal/federal_reviewer_log.md:347: - build_any.py backed up to u13/backups/build_any_pre114.py (hash appended); P keys 9930, 993F, DYH, D3019 added.
artifacts/federal/federal_reviewer_log.md:348: - Sources read by me: 5-A DCMR 3019 in full (16 lines); DYRS handbook (sha16 769fb38b1e1b0dfa, 10834 lines) read in part: lines 1455-1470, 1948-1965, 2044-2060, 3052-3066, 6060-6130.
artifacts/federal/federal_reviewer_log.md:349: - Federal_Counterparts_DC-114_126-133_2026-10-22.csv: 9 rows (130, 133 NONE FOUND; rest PARTIAL), 9-row map, NOTE M-1, CORRECTION 1 (one line-break quote in M-1). Check 81/1 (superseded)/2, sha16 66aeb1f68485b816.
artifacts/federal/federal_reviewer_log.md:350: - Next: DC-134 onward.
artifacts/federal/federal_reviewer_log.md:351: 
artifacts/federal/federal_reviewer_log.md:352: ## 2026-10-22T04:52:02Z (2026-10-21 21:52 PDT) IDA 04:46, 04:47, 04:49 items
artifacts/federal/federal_reviewer_log.md:353: - CORRECTION to my scope estimate: earlier estimate "DC-145 to 191" for awaiting-Federal rows was wrong; actual missing set is DC-114 and DC-126 to 231 (107 rows), per status.md line 184.
artifacts/federal/federal_reviewer_log.md:354: - NV-L2-205-223: NOTE M-4 (NRG24:1128-1130 condition, eligible for IV-E maintenance payments, sec. 472; point (c) item (3) rechecked; carry-over to admin route UNRESOLVED) and NOTE H-1 (NRG24 host status from my capture log: UNRESOLVED 04:24:28Z, CONFIRMED by hash 04:42:14Z; IDA's 04:23 and 04:40 differ). Check 134/4 (superseded)/0, sha16 dc3defa85b1dd1ab.
artifacts/federal/federal_reviewer_log.md:355: - DC-251-261: NOTE Y-2 (DC-253; 5-A DCMR 3001.16-17 vs 300.102(a)(2), Yudien, S47). Narrowed, not closed. 3099 keyword-only: correctional/incarcerat/jail 0. Check 187/0/6, sha16 7f57d4971337111c. P key D3001 added after backup build_any_pre_y2.py.
artifacts/federal/federal_reviewer_log.md:356: - Order note: IDA 04:47/04:49 asked for these before batch 1; they arrived after batch 1 (DC-114, 126-133) was built. Batches of about 20 from here.
artifacts/federal/federal_reviewer_log.md:357: - IDA 04:43 re-send (200.306, Yudien image): already done at 04:44Z.
artifacts/federal/federal_reviewer_log.md:358: 
artifacts/federal/federal_reviewer_log.md:359: ## 2026-10-28T15:55:37Z (2026-10-28 08:55 PDT) DC-134 to DC-153 batch (per IDA restart 2026-10-28 15:48Z)
artifacts/federal/federal_reviewer_log.md:360: - Output: Federal_Counterparts_DC-134-153_2026-10-28.csv (20 rows, per-row map, NOTE M-1). Checker: verified 99 failed 0 unpinned 0. sha256 prefix 01987f957ffc8048.
artifacts/federal/federal_reviewer_log.md:361: - Sources read by IDEA Federal: DYRS handbook lines with context; DYRS web pages New Beginnings, Your Rights and Role, Care Coordination (full); CFSA QRG Educational Stability 2011 (full); AI CFSA-10-10 (full); Education Practice Guide 2010 (lines 1-80, 208-224); AI CFSA-23-1 (lines 1-125). Capture hashes match the matrix records.
artifacts/federal/federal_reviewer_log.md:362: - build_any.py backed up to u13/backups/build_any_pre134.py (hash appended); P keys QRG, AI1010, S14, S16a, DNB, DRR, DCC added.
artifacts/federal/federal_reviewer_log.md:363: - Statuses: SUPPLIED 0; PARTIAL 12 (135, 137, 138, 139, 140, 144, 148, 149, 150, 151, 153); NONE FOUND 8 (134, 136, 141, 142, 143, 145, 146, 147, 152; 142, 143, 152 within Part 300 with RELATED FEDERAL BASELINE (outside IDEA)).
artifacts/federal/federal_reviewer_log.md:364: - Recorded, not resolved: AI CFSA-10-10 page 2 header prints CFSA-10-11; surrogate appointer OSSE (2010 guide) vs LEA or court (2023 AI); records period 2 business days (2011 QRG) vs 48 hours (2010 guide); BID lead CFSA (2023 AI) vs LEA with child welfare POC (NRG 2024, agency guidance, not law); NBYDC Maryland address.
artifacts/federal/federal_reviewer_log.md:365: - Held after this batch until IDA confirms.
artifacts/federal/federal_reviewer_log.md:366: - CORRECTION 2026-10-28T15:55:40Z (2026-10-28 08:55 PDT): the status counts in the line above are wrong; the correct counts are PARTIAL 11 and NONE FOUND 9 (row lists unchanged).
```

## Appendix B. Status lines (artifacts/federal/status.md, all lines)

```
artifacts/federal/status.md:1: 
artifacts/federal/status.md:2: - 2026-10-21 21:21 UTC / 14:21 PDT: Peer review filed at peer_review/IDEA_Federal_counterpart_review.md. 370 cells: 160 ACCEPT, 32 ACCEPT WITH FIX, 3 REJECT, 34 UNRESOLVED, 141 NO CITE (not assessed).
artifacts/federal/status.md:3: - 2026-10-21 21:25 UTC / 14:25 PDT: U.S.C. batch 1 read (12 sections); review appended; totals A168/AWF34/R3/U24, NC141.
artifacts/federal/status.md:4: - 2026-10-21 21:26 UTC / 14:26 PDT: All 15 govinfo U.S.C. captures read in full (42 USC 671, 20 USC 6311, 6312 added). Next: Fry slip opinion, then case PDFs.
artifacts/federal/status.md:5: - 2026-10-21 21:26 UTC / 14:26 PDT: Fry read; 3 case PDFs remain (Endrew F., Honig, Rowley).
artifacts/federal/status.md:6: - 2026-10-21 21:27 UTC / 14:27 PDT: Endrew F. read; Honig and Rowley remain.
artifacts/federal/status.md:7: - 2026-10-21 21:28 UTC / 14:28 PDT: Honig read; Rowley remains.
artifacts/federal/status.md:8: - 2026-10-21 21:28 UTC / 14:28 PDT: All 4 case PDFs read in full (Fry, Endrew F., Honig, Rowley). Next: IDA request for UT/NV/DC federal counterparts.
artifacts/federal/status.md:9: - 2026-10-21 21:31 UTC / 14:31 PDT: IDA counterparts request done; Federal_Counterparts_UT_NV_DC_2026-10-21.{md,csv}.
artifacts/federal/status.md:10: - 2026-10-21 21:34 UTC / 14:34 PDT: Counterpart UNRESOLVED cells updated; 1 remains (UP-08).
artifacts/federal/status.md:11: - 2026-10-21 21:35 UTC / 14:35 PDT: UJ-15..17 done.
artifacts/federal/status.md:12: - 2026-10-21 21:36 UTC / 14:36 PDT: UPDATE3 done.
artifacts/federal/status.md:13: - 2026-10-21 21:39 UTC / 14:39 PDT: UPDATE4 done.
artifacts/federal/status.md:14: - 2026-10-21 22:25 UTC / 15:25 PDT: Reassessed GA-39..GA-56 against 34 CFR (new captures 300.7,.10,.23,.105,.106,.108,.109,.113,.119,.175,.221,.227,.601,.641,.645; 20 USC 1416). A4/AWF12/NC2. Totals now A172/AWF46/R3/U6 = 227 assessed, NC143, 370 cells. GA rule text not read by me; verdicts rest on IDEA Georgia's quotes.
artifacts/federal/status.md:15: - 2026-10-21 23:25 UTC / 16:25 PDT: (1) UPDATE5.csv written: 40 NV L2 rows (NV-L2-001..040), SUPPLIED 6 / PARTIAL 19 / NONE FOUND 15; UNRESOLVED points inside rows: 300.302 not read, MOUs and Attachments A/B not in hand, NRS sections not read. Re-read in full this turn: 300.2, .13, .17, .22, .30, .39, .43, .45, .101, .104, .301, .323, .503, .519, .530, .610, .622; excerpts only of .114, .116, .154, .320, .324, .102, .8, 99.31, 42 USC 675, 1232g. Row NV-L2-007 prints '(300.13)' for Confinement; 34 CFR 300.13 is 'Elementary school' (inference: Nevada policy number; IDEA Nevada to confirm). (2) Appended IDEA Georgia's answers on GA-41/47/45 and the GA-41 'previous LEA' vs 'previous public agency' comparison item to the canonical review; counts unchanged. (3) Created Federal_Baseline_Index_2026-10-21.md: 120 CFR lines (32 coded from text re-read now, 88 TO CODE), 17 statutes and 4 cases TO CODE. Read in full now: 300.7, .23, .105, .106, .108, .109, .113, .119, .175, .221, .227, .601, .641, .645. 20 USC 1416 read-in-full status not stated in log: VERIFY.
artifacts/federal/status.md:16: - 2026-10-21 23:26 UTC / 16:26 PDT: Correction note written (Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE5_correction.md): NV-L2-007 '(300.13)' is Nevada DCFS/JJS 300.13 (Confinement) per IDEA Nevada, not JJS 500.13 as I inferred. Status and 300.530 comparison unchanged.
artifacts/federal/status.md:17: 
artifacts/federal/status.md:18: ## 2026-10-21 23:31 UTC / 16:31 PDT
artifacts/federal/status.md:19: - UPDATE6 written: Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE6.csv (SHA-256 71353f0fd658c762...). UT v3 rows UJ-19..UJ-38: SUPPLIED 5, PARTIAL 13, NONE FOUND 2. UNRESOLVED inside rows: 34 CFR 99.4 (UJ-20), 20 USC 1232h (UJ-37), not captured.
artifacts/federal/status.md:20: - 34 CFR 300.302 captured (eCFR versioner, 2026-10-13; xml SHA-256 09fae1e0d8720cdb...) and read in full. NV-L2-002 point closed by append to UPDATE5_correction.md; row stays PARTIAL.
artifacts/federal/status.md:21: - Baseline index: 88 CFR lines coded from full re-reads; all 120 CFR lines CODED. 20 USC 1416 VERIFY resolved (read in full). Statutes (17) and cases (4) still TO CODE. Index SHA-256 now 303dd21146fa2c53...
artifacts/federal/status.md:22: 
artifacts/federal/status.md:23: ## 2026-10-22 00:22 UTC / 17:22 PDT, IDEA Federal
artifacts/federal/status.md:24: - UPDATE7 written: Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE7.csv (sha256 ae0a9bf9a8ab4375...), UT v3 rows UJ-39 to UJ-76 (38 rows): SUPPLIED 18, PARTIAL 18, NONE FOUND 2 (UJ-42 dual enrollment, UJ-58 restraint/seclusion). Every quoted federal string checked programmatically against captured text (93 quoted strings, all found). Comparison items, not findings.
artifacts/federal/status.md:25: - Mapping checks requested by IDA: III.C.1.b (UJ-69) to 300.323(e) verified; 300.323(f) is interstate and not supplied. IV.U.2 (UJ-63) to 300.520(a)(2) verified (permissive; (a)(2) sits under the age-of-majority lead-in, structural note recorded). VI.K (UJ-71) to 300.2(b)(1)(iv) only partly fits (correctional facilities); added 300.2(b)(1)(iii), .101(a), .111, .114(a)(2)(i), .154. II.C.1.b (UJ-67) maps to 300.300(a)(2), not 300.519. Disagreements recorded, not resolved.
artifacts/federal/status.md:26: - New captures, read in full: 34 CFR 300.162, .167, .168, .169, .200, .201, .202, .203, .327, 99.4, 99.22 (eCFR 2026-10-13; logged in src/CFR_CAPTURE_LOG_GA39_56.txt); 20 U.S.C. 1232h (govinfo USCODE-2024; logged in src/usc/CAPTURE_LOG.txt).
artifacts/federal/status.md:27: - UJ-20 (99.4) and UJ-37 (1232h) UNRESOLVED points closed by append-only notes in Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE6_correction.md (sha256 e17639674d42ba2d...). UPDATE6 not edited. Statuses unchanged (UJ-20 SUPPLIED, UJ-37 PARTIAL).
artifacts/federal/status.md:28: - Index: 300.621 note on 99.22 closed by appended change note (Federal_Baseline_Index_2026-10-21.md sha256 543c043736b9abab...).
artifacts/federal/status.md:29: - GA currency lead logged: GA 160-4-7-.21(12) brackets 34 CFR 300.10; src/cfr_300.10.txt (eCFR 2026-10-13, xml sha256 33b3c8181e8b87fb...) reads in full: "§ 300.10 [Reserved]". Comparison item on currency only, not a finding; already noted at peer_review/IDEA_Federal_counterpart_review.md lines 509, 523.
artifacts/federal/status.md:30: - Still open: 34 CFR 300.165 (UJ-76), 300.602-.608, 300.130-.144 other than .130/.137, 104.3; ESEA Title I-D text (UJ-49); coding of 17 statutes and 4 cases in the index (next).
artifacts/federal/status.md:31: 
artifacts/federal/status.md:32: ## 2026-10-22 00:33 UTC / 17:33 PDT, IDEA Federal
artifacts/federal/status.md:33: - IDEA DC disagreements answered (appended to peer_review/IDEA_Federal_counterpart_review.md and Federal_Counterparts_UT_NV_DC_2026-10-21.md): DC-049, IDEA DC correct, 300.301(b) reads 'either a parent of a child or a public agency may initiate a request'; my 'State agency or LEA' paraphrase was inaccurate; corrected note recorded, status SUPPLIED unchanged. DC-077, MOA VI.C.4 designates the letter as prior written notice; compared with 300.503(b)-(c), text read names only 'the information used to make the decision' (partial match to (b)(3)); recipient and timing comparison items; status PARTIAL unchanged. MOA read: lines 415-440 only.
artifacts/federal/status.md:34: - UPDATE8 written: Federal_Counterparts_UT_NV_DC_2026-10-21_UPDATE8.csv (sha256 c12c46a29cd52017...), UJ-77 to UJ-80: SUPPLIED 3 (UJ-78, -79, -80; 300.151-.153), NONE FOUND 1 (UJ-77 DCFS MIS). 24 quoted strings checked against captured text, all found.
artifacts/federal/status.md:35: - Captured and read in full: 34 CFR 300.165, 300.602-.608, 104.3. Notes appended: UPDATE7_correction.md (sha256 e6203453bf4534ea...; UJ-76 300.165 closed, 1232d(b)(7) UNRESOLVED; UJ-41 adds 300.608; UJ-70 adds 300.607) and NV-JJ-006 104.3 note in Federal_Counterparts_UT_NV_DC_2026-10-21.md.
artifacts/federal/status.md:36: - Next: index coding of 17 statutes and 4 cases.
artifacts/federal/status.md:37: - 2026-10-22 00:33 UTC / 17:33 PDT: Index coding addendum appended: 300.165, 300.602-.608, 104.3, 20 U.S.C. 1417, 1436, 42 U.S.C. 11434a coded from full re-reads this turn. 15 statutes and 4 cases still TO CODE.
artifacts/federal/status.md:38: - 2026-10-22 00:34 UTC / 17:34 PDT: Captured and read in full 20 U.S.C. 1232d (govinfo). UJ-76 1232d(b)(7) point closed in UPDATE7_correction.md (60/30 days in (b)(7)(B)); status PARTIAL unchanged.
artifacts/federal/status.md:39: - 2026-10-22 00:36 UTC / 17:36 PDT: Captured 20 U.S.C. 1232d. Index addendum 2 coded from full re-reads: 1232d, 1418, 794, 1416, 1413, 1401, 1232g, 1232h, 6312, 675, 1414, 1415. DC-049 supplement appended (1414(a)(1)(B) vs 300.301(b) wording). Remaining: 1412, 7801, 671, 6311; four cases; IDA DC 5-A30 request queued.
artifacts/federal/status.md:40: - 2026-10-22 00:37 UTC / 17:37 PDT: Addendum 2 statute coding complete from full re-reads: added 1412, 7801, 671, 6311 (after 675, 1414, 1415). Index sha16 ee90c09b69e57d8d. Quotes spot-verified against src. Next: four cases (Fry, Endrew F., Honig, Rowley), then IDA DC 5-A30 UPDATE9 and DC rows 41-80 response.
artifacts/federal/status.md:41: - 2026-10-22 00:38 UTC / 17:38 PDT: Addendum 2 case coding complete from full re-reads of official text: Endrew F. (slip op.), Fry (slip op.), Honig (484 U.S. 305), Rowley (458 U.S. 176). Quotes verified against src. Text notes: Fry src 'words(?)' artifact; Honig OCR lacks most page numbers (syllabus ranges used); U.S. Reports cites for Endrew F. and Fry remain from memory, unverified. Index sha16 408782a28eed9ddc. Next: IDA DC 5-A30 counterpart request (UPDATE9) and DC rows 41-80 response.
artifacts/federal/status.md:42: - 2026-10-22 00:41 UTC / 17:41 PDT: IDA 5-A30 request done. eCFR recapture 300.300, 300.324, 300.33, 300.8 (version 2026-10-13; first attempt returned HTTP 406, logged and corrected in CFR_CAPTURE_LOG). UPDATE9 (4 rows, sha16 cd14d2657a87d2d9). Response to IDEA DC rows 41-80 review: peer_review/IDEA_Federal_response_DC_rows41-80_2026-10-22.md, including a correction to my DC-078 675(1)(G) lead.
artifacts/federal/status.md:43: - 2026-10-22 00:42 UTC / 17:42 PDT: IDA 00:40Z requests done: UPDATE10 (3 rows, sha16 66265b4666dce91e): 300.530(i) definitions, 300.535 NONE FOUND in 3043, expert fees PARTIAL with Arlington UNRESOLVED (no official copy). Response file addendum appended.
artifacts/federal/status.md:44: - 2026-10-22 00:44 UTC / 17:44 PDT: IDA 00:43 items done. Index correction note: Endrew F. and Fry reporter cites UNRESOLVED (slip-op cites only; queue with Arlington). Captured and read 42 USC 672 (govinfo), 45 CFR 1355.20 (eCFR), Pub. L. 108-335 sec. 327 (govinfo). UPDATE11 (2 rows, sha16 62dfdac81b2471f5). Official/Lexis queue: Arlington No. 05-18; Endrew F. No. 15-827 and Fry No. 15-497 U.S. Reports pages. Next: coding queue.
artifacts/federal/status.md:45: 
artifacts/federal/status.md:46: - 2026-10-22T01:08:30Z (2026-10-21 18:08 PDT): UPDATE12 batches 1-2 written (18 rows, sha16 349a81a3add3dbed). Batches 3-4 pending.
artifacts/federal/status.md:47: - 2026-10-22T02:17:28Z (2026-10-21 19:17 PDT): ruling noted; quote line map UPDATE12_quote_line_map_2026-10-22.md (sha16 f945186e37ee0c0b).
artifacts/federal/status.md:48: - 2026-10-22T02:18:23Z (2026-10-21 19:18 PDT): UPDATE12 batch 3 (DC-098..104 less 100), 6 rows; CSV sha16 cd7e5f0f95714c50.
artifacts/federal/status.md:49: - 2026-10-22T02:19:51Z (2026-10-21 19:19 PDT): UPDATE12 batch 4a (DC-105..113), 9 rows; CSV sha16 b9b01cbc87443cc2.
artifacts/federal/status.md:50: - 2026-10-22T02:21:05Z (2026-10-21 19:21 PDT): UPDATE12 batch 4b; DC-081..125 complete. CSV sha16 5d470b433409e05e.
artifacts/federal/status.md:51: - 2026-10-22T02:22:41Z (2026-10-21 19:22 PDT): UJ-81/82 counterparts, Federal_Counterparts_UT_UJ81-82_2026-10-22.csv sha16 e7efbc27ac6f5f8a.
artifacts/federal/status.md:52: - 2026-10-22T02:23:19Z (2026-10-21 19:23 PDT): append-only record of the 300.34/300.300 cell edits in federal_reviewer_log.md.
artifacts/federal/status.md:53: - 2026-10-22T02:24:09Z (2026-10-21 19:24 PDT): created Federal_notes_UJ82-300.228_UJ60-300.519_2026-10-22.md (sha16 5a62960fd38acfb6): 300.228 resolved; UJ-60 bearing on 300.519(d)(2)(i) (inference, UNRESOLVED).
artifacts/federal/status.md:54: - 2026-10-22T02:24:16Z (2026-10-21 19:24 PDT): appended correction note to Federal_notes_UJ82-300.228_UJ60-300.519_2026-10-22.md (sha16 eddd6f2eb3374283).
artifacts/federal/status.md:55: - 2026-10-22T03:13:03Z (2026-10-21 20:13 PDT): appended INFERENCE label for line 28 to Federal_notes_UJ82-300.228_UJ60-300.519_2026-10-22.md (sha16 913598241fa757b6).
artifacts/federal/status.md:56: - 2026-10-22T03:15:06Z (2026-10-21 20:15 PDT): created Federal_item3_leftovers_DC_2026-10-22.md (sha16 1f296f451838c4f8). Item 3 leftovers L1-L5 done. New captures: 300.208, .138, .18 (reserved), .622, .320, 34 CFR 99.31.
artifacts/federal/status.md:57: - 2026-10-22T03:18:57Z (2026-10-21 20:18 PDT): created Federal_Counterparts_DC232-250_UP11_2026-10-22.csv (sha16 697e4499fa834552): DC-232..250 + UP-11 federal counterparts, 85/85 quotes verified.
artifacts/federal/status.md:58: - 2026-10-22T03:20:24Z (2026-10-21 20:20 PDT): created Federal_Counterparts_UP12-13_2026-10-22.csv (sha16 79d62428dadd36d6): UP-12, UP-13, 17/17 quotes verified.
artifacts/federal/status.md:59: - 2026-10-22T03:22:30Z (2026-10-21 20:22 PDT): created Federal_Counterparts_NV-L2-109-162_2026-10-22.csv (sha16 4d087e40b5b2ae33): NV-L2-109..162 counterparts (6 grouped rows), 37/37 quotes verified.
artifacts/federal/status.md:60: - 2026-10-22T03:24:09Z (2026-10-21 20:24 PDT): created Federal_Cases_official_2026-10-22.md (sha16 43f29d5f078fd465): 4 cases from supremecourt.gov, 7/7 quotes verified.
artifacts/federal/status.md:61: - 2026-10-22T03:26:07Z (2026-10-21 20:26 PDT): appended per-row map + 3 update rows to Federal_Counterparts_NV-L2-109-162_2026-10-22.csv (sha16 ef2fc8c2346f2339); 27/27 quotes verified.
artifacts/federal/status.md:62: - 2026-10-22T03:28:17Z (2026-10-21 20:28 PDT): 300.168 re-captured, no truncation; GA-82..85 counterparts written (33/33).
artifacts/federal/status.md:63: - 2026-10-22T03:29:40Z (2026-10-21 20:29 PDT): wrote Federal_Schaffer_burden_leads_2026-10-22.md (sha16 e06903857ccd3295); item (3) Schaffer leads, 4 states; correction C-1 appended (pins).
artifacts/federal/status.md:64: - 2026-10-22T03:31:15Z (2026-10-21 20:31 PDT): wrote Federal_672_agreement_facts_2026-10-22.md (sha16 e9dff1ce704a559a): item (4) 672 agreement facts; 14/14 quotes verified after C-1.
artifacts/federal/status.md:65: - 2026-10-22T03:31:23Z (2026-10-21 20:31 PDT): 672 file C-2 appended (sha16 b32447c8bc550156).
artifacts/federal/status.md:66: 
artifacts/federal/status.md:67: ## 2026-10-22T03:33:52Z (2026-10-21 20:33 PDT) IDA 03:30 items (a)-(c)
artifacts/federal/status.md:68: - (a) Federal_Counterparts_UP14-15_2026-10-22.csv (sha16 b4f9b0a1963b9661): UP-14 PARTIAL (300.101(a), 300.323(e)-(f), 675(1)(G)); UP-15 SUPPLIED on its face, scope UNRESOLVED; 13/13 quotes verified; per-row map appended.
artifacts/federal/status.md:69: - (b) Federal_NAC388.283_vs_300.519h_2026-10-22.md (sha16 1d76086238447e74): same 30-day clock; actor differs (public agency vs SEA), appointment vs assignment, trigger wording differs.
artifacts/federal/status.md:70: - (c) Federal_Counterparts_NV-L2-163-185_2026-10-22.csv (sha16 30d3e5531826347c): 3 groups (500.17 PARTIAL/NONE FOUND; 500.18 PARTIAL/NONE FOUND; 500.19 NONE FOUND keyword-only); 23/23 quotes verified; 23-row per-row map appended.
artifacts/federal/status.md:71: - New captures (eCFR, HTTP 200): 300.302, 300.610, 300.611, 300.623.
artifacts/federal/status.md:72: - Builder: src/u13/build_any.py with rows_up1415.py, rows_nv163.py.
artifacts/federal/status.md:73: 
artifacts/federal/status.md:74: ## 2026-10-22T03:37:12Z (2026-10-21 20:37 PDT) IDA 03:34 items (1)-(3)
artifacts/federal/status.md:75: - (1)+(2) Federal_Counterparts_GA-89_GA-48burden_2026-10-22.csv (sha16 b2729b6736789cc8): GA-89 PARTIAL (DJJ fifth surrogate ground, short-term or temporary foster assignment, has no 300.519(a) counterpart; 300.30(a)(2) "unless" route; GA rule .11 lists only the four federal grounds; GA definition (31) omits the "unless" clause); GA-48 burden item PARTIAL vs Schaffer, 546 U.S. at 61-62. 17/17 quotes verified; map appended.
artifacts/federal/status.md:76: - (3) Federal_Counterparts_NV-L2-186-204_2026-10-22.csv (sha16 8d203688f48a0b0b): 600.02 NONE FOUND (keyword); CCJJS PARTIAL 193/194/196/198; Washoe PARTIAL 202/203/204. 34/34 quotes verified; 19-row map appended.
artifacts/federal/status.md:77: - Builder src/u13/build_any.py (keys added: 546bv, N6002, CC, WA); rows_ga89.py, rows_nv186.py.
artifacts/federal/status.md:78: 
artifacts/federal/status.md:79: ## 2026-10-22T03:38:37Z (2026-10-21 20:38 PDT) IDA 03:35 PA items
artifacts/federal/status.md:80: - (1) Federal_Counterparts_DC232-250_UP11_2026-10-22.csv: appended C-1 (DC-242 plural phrases at 324 line 32, singular at line 35). sha16 697e4499fa834552 -> 2a99ed57168c3bda.
artifacts/federal/status.md:81: - (2) Same file: appended N-1 checker note. New widened checker src/u13/check_csv.py (every cell; pin before or after). Before the appends: 86 verified, 0 failed, 30 unpinned. PA count 87 not reconciled. Today's four new files re-run: 13/23/17/34 verified, 0 failed.
artifacts/federal/status.md:82: - (3) CFR_CAPTURE_LOG_GA39_56.txt: appended full URL, HTTP 200 and full sha256 for 546bv.pdf and 548bv.pdf. A re-fetch matched the stored bytes.
artifacts/federal/status.md:83: - GA-89, GA-48 and NV 186-204 were already done at 03:37Z (see the entry above).
artifacts/federal/status.md:84: 
artifacts/federal/status.md:85: ## 2026-10-22T03:40:38Z (2026-10-21 20:40 PDT) IDA 03:38 item (B)
artifacts/federal/status.md:86: - Federal_Counterparts_UP16-20_2026-10-22.csv (sha16 da901b9c6da26df4): UP-16 PARTIAL; UP-17 SUPPLIED on its face vs 675(1)(G)(i); UP-18 PARTIAL (675(1)(B) not read); UP-19 SUPPLIED with one item PARTIAL (best-interest factors, transportation-cost rule and dispute rule not found in 6311/6312 as read; ED/HHS 2016 guidance not captured); UP-20 PARTIAL. ESSA is labeled a related federal baseline. Builder checker 56/56; widened checker run; map appended. ESSA was already captured from govinfo (CAPTURE_LOG lines 9-10). Item (A) was done at 03:38:37Z.
artifacts/federal/status.md:87: 
artifacts/federal/status.md:88: - 2026-10-22 03:44 UTC (20:44 PDT): UP-18 U-1 appended to Federal_Counterparts_UP16-20 (HR4980 link KEPT; H.R. 4980 = Pub. L. 113-183 per govinfo PLAW header line 9; rights document is 42 U.S.C. 675a(b)(1)-(2), added by sec. 113(d), not 675(1)(B); 675a and PLAW-113publ183 captured from govinfo 03:41:16Z, HTTP 200). UP-19 U-1 appended: ED/HHS NRG June 23 2016 captured from acf.hhs.gov (redirect to acf.gov), sha256 a674eb14...eb6d, 28 pp, AGENCY GUIDANCE, NOT LAW; Q12 factors, line 530 transportation costs, lines 872-873 disputes match the flyer; ed.gov copies HTTP 403. File now 74 verified, 0 failed, 9 unpinned; sha16 4405d26f939ba7a6. New file Federal_Counterparts_GA-90-91_2026-10-22.csv (sha16 cc240f4d42470028): GA-90 NONE FOUND for an IDEA interagency team (method stated; Part 303 not searched), PARTIAL on LEA seat vs 300.321; GA-91 PARTIAL vs 300.111/300.301. 23/23 quotes verified at build; map present.
artifacts/federal/status.md:89: - 2026-10-22 03:44 UTC: correction to the entry above: the map rows were appended after the build (the builder does not write G); Federal_Counterparts_GA-90-91_2026-10-22.csv now sha16 fbc8f78d7ae9acba, 3 MAP rows.
artifacts/federal/status.md:90: - 2026-10-22T03:46:22Z (2026-10-21 20:46 PDT): Schaffer leads C-1 (UT burden search command recorded, undue-burden statement withdrawn, Title 80 hits listed, UT statement stays UNRESOLVED) and C-2 (Provo quote L294-296, not L104) appended; capture-log note for row 19 (300.168 .txt sha256 cd4f40cb...a172) appended.
artifacts/federal/status.md:91: - 2026-10-22 03:50 UTC (20:50 PDT): GA-90 U-1 appended (Part 303 captured from eCFR 03:47:05Z, 5087 lines; NONE FOUND for a local team; 303.600 State ICC is a different body); GA-90-91 file sha16 80df7988f4c39aa7, 28 verified. New Federal_Counterparts_GA-92-94_UP21-22_2026-10-22.csv (sha16 0e71c3dd595a2015): GA-92 PARTIAL vs 300.30(a)(3), (b)(2); GA-93 PARTIAL vs 300.323(e), (g), ESSA 6311(g)(1)(E) related baseline; GA-94 PARTIAL vs 300.613-.625, 99.31(a), (a)(9), 1232g(b)(1)(L) and (b)(2)(B) (99.31 has no caseworker or dependency text, keyword-only); UP-21 NONE FOUND (method stated), related 300.39(b)(1), 300.17(a); UP-22 PARTIAL vs 1232g(b)(1)(L), 99.31(a)(5)/99.38, (a)(9), 300.622(a). New eCFR captures: 300.17, .39, .613-.621, .624, .625.
artifacts/federal/status.md:92: - 2026-10-22 03:51 UTC (20:51 PDT): UP16-20 C-2 appended (APA ellipsis corrections for truncated quotes in UP-18 U-1 and UP-19 U-1, incl. [675a:29], [675:14], [PL183:603], [NRG16:530]; P300 col 5 split re-pinned to 1018-1019). Checker v2 (ellipsis-aware); trunc_scan.py added. Federal_Counterparts_UP16-20_2026-10-22.csv sha16 01d6427192f783e2. Queued: truncation scan of all earlier 2026-10-22 files.
artifacts/federal/status.md:93: - 2026-10-22T03:56:18Z (2026-10-21 20:56 PDT): IDA 03:53 items.
artifacts/federal/status.md:94:   - (1) Checker v3 (src/u13/check_csv.py) reads the pin list from the project copy src/u13/build_any.py and pairs pins across "(" or ")". v1 is kept as src/u13/check_csv_v1.py.
artifacts/federal/status.md:95:   - Keys appended to build_any.py (project and /tmp copies identical): UT, UT201, UT104 (from build_up.py and the UJ81-82 source), plus 672, 1355, GA248, NV501, UT512.
artifacts/federal/status.md:96:   - DC232-250: N-2 appended (sha16 8d1f57bf8512e2f2). The counts reconcile: the body gives 86 under v1 and 87 under v3 (DC-236 [33:2] now paired, matching the PA's 87); C-1 adds 2, for 89. The checker now reads 90 because N-2 quotes the DC-236 phrase.
artifacts/federal/status.md:97:   - UP12-13: the 5 failures were caused by missing keys UT201 and UT104. Now 17 verified, 0 failed.
artifacts/federal/status.md:98:   - UT_UJ81-82: the 18 failures were caused by the missing UT key. 1 real pin error remains: UJ-82 "State complaint" [UT:5293] should be [UT:5293-5294]. C-1 appended (sha16 f1f6737408ef6496). The checker now reads 2 failed, because C-1 quotes the wrong pin.
artifacts/federal/status.md:99:   - The UJ81-82 and UP12-13 files lack per-row map rows. Open.
artifacts/federal/status.md:100:   - (3) 672 file: C-3 appended. The recount gives 16 pinned source quotes in the body, all verified; the PA is right and my 14 was wrong. The NV 316-317 ellipsis is replaced by the joined form.
artifacts/federal/status.md:101:   - (4) A-1 appended: NV/welfare/sources/L2_NDE_ESSA_AB491.txt L96-110 (NDE slides, Aug 18 2017). They describe a WCSD-WCDSS MOU with "Transportation to School of Origin to be funded through Title IV-E (2017)" [103]. The federal hook is 675(4)(A) [675:38]. This does not change "no CW-JJ IV-E agreement captured" (INFERENCE: an education to child welfare transport MOU). The MOU text is not captured. 672 file sha16 dd6b97abc8bc6a40.
artifacts/federal/status.md:102:   - sha256 for the 675a and PL183 .htm/.txt captures appended to src/usc/CAPTURE_LOG.txt.
artifacts/federal/status.md:103: - 2026-10-22T03:56:53Z (2026-10-21 20:56 PDT): trunc_scan run over all 12 Federal_Counterparts_*2026-10-22.csv. Raw output in TRUNC_SCAN_raw_20261022T035653Z.txt; a mechanical filter dropping list-item ends (; and / ; or / dash / colon / comma) and next-is-punctuation leaves the flags in TRUNC_SCAN_review_20261022T035653Z.txt. Not yet reviewed by reading; a flag is not a finding (a phrase quote may end mid-sentence under APA 7). Row-by-row review open.
artifacts/federal/status.md:104: - 2026-10-22T04:01:14Z (2026-10-21 21:01 PDT): IDA 03:58 items.
artifacts/federal/status.md:105:   - Per-row maps appended: UJ81-82 (UJ-81 IV.E with 300.151-.153; UJ-82 IV.F with 300.506) and UP12-13 (UP-12, UP-13 with 300.30, .300, .519, plus "no counterpart within group" items and the method). Maps were appended before the M-1 notes.
artifacts/federal/status.md:106:   - Meaning-test scan. This replaces the end-truncation scan logged earlier; TRUNC_SCAN_* files are superseded and kept.
artifacts/federal/status.md:107:     - Tool: src/u13/meaning_scan.py.
artifacts/federal/status.md:108:     - Scope: the 18 Federal files dated 2026-10-22 (12 CSV, 6 MD).
artifacts/federal/status.md:109:     - Method: for each pinned quote that verifies, take the omitted text in the same clause before and after it (clause bounded by ". ", ";" or a subparagraph marker). Flag it when that text holds a negation, condition, exception or qualifier term and the qualifier is not already carried in the same cell.
artifacts/federal/status.md:110:     - Results: 510 quotes scanned; 131 machine candidates (MEANING_SCAN_candidates_20261022.txt), all read by me.
artifacts/federal/status.md:111:     - 21 quote instances in 16 row items have an omitted qualifier that bears on the comparison. 1 of them, DC-248, is possible (the clause it attaches to is UNRESOLVED).
artifacts/federal/status.md:112:     - Corrections appended as "MEANING NOTE M-1 (<row>)" in 7 files:
artifacts/federal/status.md:113:       - DC232-250: DC-237, -241, -248, -249.
artifacts/federal/status.md:114:       - GA-92-94: GA-93, GA-94.
artifacts/federal/status.md:115:       - NV-L2-109-162: NV-L2-129, -138, -077/083/084.
artifacts/federal/status.md:116:       - NV-L2-186-204: NV-L2-186, -199.
artifacts/federal/status.md:117:       - UP12-13: UP-13.
artifacts/federal/status.md:118:       - UP14-15: UP-15.
artifacts/federal/status.md:119:       - UJ81-82: UJ-81.
artifacts/federal/status.md:120:     - Every new quote in M-1 verifies (checker v3).
artifacts/federal/status.md:121:     - Limits: keyword-based triggers, so a qualifier phrased without a listed term is not caught. Unpinned quotes are not scanned. Older (pre-10-22) files are not scanned.
artifacts/federal/status.md:122:     - No ellipses were added in bulk.
artifacts/federal/status.md:123: - 2026-10-22T04:12Z (21:12 PDT): truncation review A-1 done (CORRECT 25, KEEP 197); Title 80 80-6-504 resolved (Schaffer C-2). Next: coding queue, 327 riders, TEAM_CONSOLIDATION briefing.
artifacts/federal/status.md:124: - 2026-10-22T04:12Z (21:12 PDT): correction to line 106: TRUNC_SCAN_* files are no longer superseded; IDA 03:59 reinstated the review file for one-by-one adjudication (A-1).
artifacts/federal/status.md:125: - 2026-10-22T04:08:33Z (2026-10-21 21:08 PDT): IDA 04:03 items done (M-3 notes, C-3, timestamp corrections, src/u13 self-contained). Next: coding queue.
artifacts/federal/status.md:126: - 2026-10-22T04:14:18Z: meaning scan adjudicated (131 lines); v2 scan run, 34 new candidates OPEN. M-3 rows added for UP-16 675G, DC-243, DC-240, NV-L2-122.
```

## Appendix C. Source records

### artifacts/federal/src/usc/CAPTURE_LOG.txt

```
artifacts/federal/src/usc/CAPTURE_LOG.txt:1: 2026-10-21T21:22:59Z 20 USC 1401 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap33-subchapI-sec1401.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:2: 2026-10-21T21:23:00Z 20 USC 1412 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap33-subchapII-sec1412.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:3: 2026-10-21T21:23:00Z 20 USC 1414 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap33-subchapII-sec1414.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:4: 2026-10-21T21:23:01Z 20 USC 1415 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap33-subchapII-sec1415.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:5: 2026-10-21T21:23:01Z 20 USC 1417 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap33-subchapII-sec1417.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:6: 2026-10-21T21:23:02Z 20 USC 1232g 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap31-subchapIII-part4-sec1232g.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:7: 2026-10-21T21:23:02Z 42 USC 671 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap7-subchapIV-partE-sec671.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:8: 2026-10-21T21:23:02Z 42 USC 675 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap7-subchapIV-partE-sec675.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:9: 2026-10-21T21:23:03Z 20 USC 6311 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap70-subchapI-partA-subpart1-sec6311.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:10: 2026-10-21T21:23:03Z 20 USC 6312 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap70-subchapI-partA-subpart1-sec6312.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:11: 2026-10-21T21:23:23Z 20 USC 1418 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap33-subchapII-sec1418.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:12: 2026-10-21T21:23:23Z 20 USC 1436 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap33-subchapIII-sec1436.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:13: 2026-10-21T21:23:24Z 20 USC 1413 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap33-subchapII-sec1413.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:14: 2026-10-21T21:23:24Z 20 USC 7801 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap70-subchapVIII-partA-sec7801.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:15: 2026-10-21T21:23:25Z 42 USC 11434a 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap119-subchapVI-partB-sec11434a.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:16: 2026-10-21T21:33:52Z 29 USC 794 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title29/html/USCODE-2024-title29-chap16-subchapV-sec794.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:17: usc_20_1416 f04228d9e55a544b 2026-10-21T22:22:48Z
artifacts/federal/src/usc/CAPTURE_LOG.txt:18: 2026-10-22T00:19:06Z 20 USC 1232h 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap31-subchapIII-part4-sec1232h.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:19: usc_20_1232h 8adc0bf180d31e2c 2026-10-22T00:19:06Z
artifacts/federal/src/usc/CAPTURE_LOG.txt:20: 2026-10-22T00:33:52Z 20 USC 1232d 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title20/html/USCODE-2024-title20-chap31-subchapIII-part3-sec1232d.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:21: usc_20_1232d c207d30047cdba5b 2026-10-22T00:33:52Z
artifacts/federal/src/usc/CAPTURE_LOG.txt:22: 2026-10-22T00:43:42Z 42 USC 672 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap7-subchapIV-partE-sec672.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:23: usc_42_672 3f1e850cd9da890e 2026-10-22T00:43:42Z
artifacts/federal/src/usc/CAPTURE_LOG.txt:24: plaw108_335 d842bdb645a40d5c 2026-10-22T00:44:03Z https://www.govinfo.gov/content/pkg/PLAW-108publ335/html/PLAW-108publ335.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:25: 2026-10-22T03:41:16Z 42 USC 675a 200 https://www.govinfo.gov/content/pkg/USCODE-2024-title42/html/USCODE-2024-title42-chap7-subchapIV-partE-sec675a.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:26: 2026-10-22T03:41:16Z Pub. L. 113-183 200 https://www.govinfo.gov/content/pkg/PLAW-113publ183/html/PLAW-113publ183.htm
artifacts/federal/src/usc/CAPTURE_LOG.txt:27: # appended 2026-10-22T03:56:18Z (2026-10-21 20:56 PDT): sha256 for the 03:41:16Z captures (hashes computed 2026-10-22T03:56:18Z)
artifacts/federal/src/usc/CAPTURE_LOG.txt:28: usc_42_675a.htm 86491a28d658113de03384c811bef1ea195f82ea23c1d207329ef5a9e476285d
artifacts/federal/src/usc/CAPTURE_LOG.txt:29: usc_42_675a.txt 8c52bcd01c40338d022bd1999cb1915ac43b514eee5e4b4406ce4fea9795f669
artifacts/federal/src/usc/CAPTURE_LOG.txt:30: plaw_113_183.htm 758b587e5302b26a4b8665e58a7d5651ee8a6386c928570cf685f093e35ac615
artifacts/federal/src/usc/CAPTURE_LOG.txt:31: plaw_113_183.txt 2bd6cfc0a48d77bf29fe19703db915f0b8c56d8531bc02a3be0dbf5bf20bb19a
```

### artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt

```
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:1: cfr_300.105 904 6f4ca3e94b02d069 2026-10-21T22:22:38Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:2: cfr_300.106 1174 580402578e27c4d5 2026-10-21T22:22:39Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:3: cfr_300.108 1448 03d26997901a8c34 2026-10-21T22:22:39Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:4: cfr_300.109 429 e20fb3883c96ea48 2026-10-21T22:22:39Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:5: cfr_300.113 1001 886a94ed9229822e 2026-10-21T22:22:44Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:6: cfr_300.119 458 1109510e267279d6 2026-10-21T22:22:45Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:7: cfr_300.175 599 26628b25f4ade787 2026-10-21T22:22:45Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:8: cfr_300.221 371 a167517bd20c4c9b 2026-10-21T22:22:45Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:9: cfr_300.227 1610 c4e5fe250b359118 2026-10-21T22:22:46Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:10: cfr_300.23 286 ee3da243b629b712 2026-10-21T22:22:46Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:11: cfr_300.601 1669 cc95d4355a1a9701 2026-10-21T22:22:46Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:12: cfr_300.641 1301 f0c923b9221d2d38 2026-10-21T22:22:47Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:13: cfr_300.645 1061 6a8de9075992b038 2026-10-21T22:22:47Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:14: cfr_300.10 21 33b3c8181e8b87fb 2026-10-21T22:22:47Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:15: cfr_300.7 291 65a1b053b8d9a949 2026-10-21T22:22:48Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:16: cfr_300.302 620 09fae1e0d8720cdb 2026-10-21T23:28:24Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:17: cfr_300.162 1936 21a110210cec4a27 2026-10-22T00:19:00Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:18: cfr_300.167 656 24a789822b9f6ee8 2026-10-22T00:19:00Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:19: cfr_300.168 2069 826007e00cb4044c 2026-10-22T00:19:00Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:20: cfr_300.169 1121 fe31afab0f6cafa0 2026-10-22T00:19:00Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:21: cfr_300.200 561 25321aaca56054af 2026-10-22T00:19:00Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:22: cfr_300.201 753 aac0c23a754c8baf 2026-10-22T00:19:00Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:23: cfr_300.202 2427 31c41d5a4aeb2980 2026-10-22T00:19:00Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:24: cfr_300.203 5591 f6c0d757916f6277 2026-10-22T00:19:00Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:25: cfr_300.327 546 afadf4cf7783e47c 2026-10-22T00:19:00Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:26: cfr_99.4 667 0d8a0c13a5dc60ba 2026-10-22T00:19:00Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:27: cfr_99.22 1652 2b058a77febe8fee 2026-10-22T00:19:00Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:28: cfr_300.165 1058 6ef3d3c60104ba7a 2026-10-22T00:31:47Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:29: cfr_300.602 2531 19da5fbef93e61e0 2026-10-22T00:31:47Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:30: cfr_300.603 1672 19abeff2b453e7ef 2026-10-22T00:31:48Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:31: cfr_300.604 4930 4a55cd6b852c61bf 2026-10-22T00:31:53Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:32: cfr_300.605 2080 e24cf610d24f2eb5 2026-10-22T00:31:53Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:33: cfr_300.606 837 63f0581869fdd70b 2026-10-22T00:31:58Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:34: cfr_300.607 1504 5c5ffb67ec23b8fe 2026-10-22T00:31:58Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:35: cfr_300.608 809 8f95bdb9f8e5707c 2026-10-22T00:31:59Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:36: cfr_104.3 7156 d38784396e0b3ebb 2026-10-22T00:31:59Z
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:37: cfr_300.300_v2 104 98445b0cb69ffb67 2026-10-22T00:39:12Z (eCFR versioner 2026-10-13; recapture for IDA 5-A30 request)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:38: cfr_300.324_v2 104 98445b0cb69ffb67 2026-10-22T00:39:12Z (eCFR versioner 2026-10-13; recapture for IDA 5-A30 request)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:39: cfr_300.33_v2 104 98445b0cb69ffb67 2026-10-22T00:39:13Z (eCFR versioner 2026-10-13; recapture for IDA 5-A30 request)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:40: cfr_300.8_v2 104 98445b0cb69ffb67 2026-10-22T00:39:13Z (eCFR versioner 2026-10-13; recapture for IDA 5-A30 request)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:41: CORRECTION 2026-10-22T00:39:23Z: the four _v2 lines above (lines 37-40) are HTTP 406 error bodies (compression required), not captures. Disregard them; recaptured below with --compressed.
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:42: cfr_300.300_v2 7394 37930ea281771c83 2026-10-22T00:39:24Z (eCFR versioner 2026-10-13, --compressed; for IDA 5-A30 request)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:43: cfr_300.324_v2 6650 5288e1a3ee62b62a 2026-10-22T00:39:24Z (eCFR versioner 2026-10-13, --compressed; for IDA 5-A30 request)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:44: cfr_300.33_v2 349 57cf7f6832c804b9 2026-10-22T00:39:24Z (eCFR versioner 2026-10-13, --compressed; for IDA 5-A30 request)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:45: cfr_300.8_v2 8141 3cfab1c8d7153126 2026-10-22T00:39:25Z (eCFR versioner 2026-10-13, --compressed; for IDA 5-A30 request)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:46: cfr_300.530_v2 7698 fab86912b99b788c 2026-10-22T00:41:30Z (eCFR versioner 2026-10-13, --compressed; IDA 00:40Z request)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:47: cfr_300.535_v2 994 07a13232af59c7c8 2026-10-22T00:41:30Z (eCFR versioner 2026-10-13, --compressed; IDA 00:40Z request)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:48: cfr_300.517_v2 4410 5c91b940c8c63161 2026-10-22T00:41:31Z (eCFR versioner 2026-10-13, --compressed; IDA 00:40Z request)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:49: cfr45_1355.20 14036 e44b51b05582cc87 2026-10-22T00:43:43Z (eCFR versioner 2026-10-13 title 45, --compressed, HTTP 200; IDA 00:43 DC-078)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:50: cfr_300.2_v2 1447 8932207aacd32c9b 2026-10-22T01:05:55Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:51: cfr_300.101_v2 1433 5c8d5271907713d6 2026-10-22T01:05:56Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:52: cfr_300.149_v2 1759 8edf22d8f2c25ec8 2026-10-22T01:05:56Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:53: cfr_300.102_v2 3043 56ad1797c650f7a6 2026-10-22T01:05:56Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:54: cfr_300.30_v2 1543 07aaa930f9243def 2026-10-22T01:05:57Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:55: cfr_300.519_v2 2761 59807b1e810cfe6a 2026-10-22T01:05:57Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:56: cfr_300.506_v2 3465 c199190d7db7efdf 2026-10-22T01:05:58Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:57: cfr_300.507_v2 1200 cc6b246a57174542 2026-10-22T01:05:58Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:58: cfr_300.508_v2 4131 e807a3f7f7925605 2026-10-22T01:05:58Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:59: cfr_300.510_v2 4042 ddb617abe88aa961 2026-10-22T01:05:59Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:60: cfr_300.518_v2 1661 2924780c4cdc0294 2026-10-22T01:05:59Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:61: cfr_300.148_v2 3798 86c6db9aefec0c18 2026-10-22T01:06:02Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:62: cfr_300.321_v2 3989 8ac12bb9f24b33da 2026-10-22T01:06:16Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:63: cfr_300.45_v2 451 d825765488ca626c 2026-10-22T01:06:50Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:64: cfr_300.151_v2 1413 40482ed390c06d92 2026-10-22T01:06:51Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:65: cfr_300.152_v2 3263 fb81a37948af979f 2026-10-22T01:06:51Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:66: cfr_300.153_v2 1531 dcd3a3d9f0c4337e 2026-10-22T01:06:52Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:67: cfr_part300_full 569165 083985015b2f3883 2026-10-22T01:06:55Z (eCFR versioner 2026-10-13 full Part 300, HTTP 200; KEYWORD SEARCH ONLY, not read in full)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:68: cfr_300.536_v2 1045 a93e12a51e67b3d5 2026-10-22T02:17:39Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:69: cfr_300.114_v2 1808 e5675f816eb823b6 2026-10-22T02:18:41Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:70: cfr_300.306_v2 2117 9faf510ab423952a 2026-10-22T02:18:42Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:71: cfr_300.310_v2 1048 6fb0dea585b31c55 2026-10-22T02:18:42Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:72: cfr_300.303_v2 778 e0f286555e1e1e60 2026-10-22T02:18:43Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:73: cfr_300.300_v2 7394 37930ea281771c83 2026-10-22T02:18:43Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:74: cfr_300.106_v2 1173 6d818c3286f0042e 2026-10-22T02:18:43Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:75: cfr_300.323_v2 4552 498dc405b69c71ae 2026-10-22T02:18:47Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:76: cfr_300.34_v2 8618 8cc34948e87ae1ba 2026-10-22T02:18:48Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:77: cfr_300.305_v2 3584 3a7fe2763118f443 2026-10-22T02:20:15Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:78: cfr_300.503_v2 2366 388572e42d449c3e 2026-10-22T02:20:16Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:79: cfr_300.502_v2 4056 6e0e25a59ca6d82f 2026-10-22T02:20:16Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:80: cfr_300.131_v2 1681 dcbe48c2bf99f1e0 2026-10-22T02:20:17Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:81: cfr_300.641_v2 1300 48159f268fdc6fb7 2026-10-22T02:20:17Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:82: cfr_300.512_v2 1951 1ddf8fb046220329 2026-10-22T02:20:17Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:83: cfr_300.156_v2 4536 193e4399a01528aa 2026-10-22T02:20:18Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:84: cfr_300.105_v2 903 c85afde8d238dab4 2026-10-22T02:20:18Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:85: cfr_300.108_v2 1447 017e87a10c5bc628 2026-10-22T02:20:19Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:86: cfr_300.228_v2 541 c0a8db38f80874f0 2026-10-22T02:23:20Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:87: cfr_300.208_v2 1549 06609ec0d138d017 2026-10-22T03:13:09Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:88: cfr_300.138_v2 2187 02f75bad6140a8a1 2026-10-22T03:13:09Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:89: cfr_300.320_v2 4726 b4f9090f10a37f2a 2026-10-22T03:13:09Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:90: cfr_300.622_v2 1317 ae29cd120734a097 2026-10-22T03:13:30Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:91: cfr34_99.31 14268 de1a82fe3b00a6f8 2026-10-22T03:13:30Z (eCFR versioner 2026-10-13 title 34 part 99, HTTP 200)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:92: cfr_300.18_v2 20 8e2b01db9b291697 2026-10-22T03:13:37Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:93: cfr_300.111_v2 2217 e17a9bc337c818c8 2026-10-22T03:15:46Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:94: cfr_300.116_v2 1242 31d34ff74c60a724 2026-10-22T03:15:47Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:95: cfr_300.325_v2 1374 bb058ac444215f86 2026-10-22T03:15:47Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:96: cfr_300.146_v2 810 1f11643ad5f18dea 2026-10-22T03:15:47Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:97: cfr_300.301_v2 1838 e6a7802a1697524a 2026-10-22T03:15:48Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:98: cfr_300.520_v2 1434 c4354097ecc81683 2026-10-22T03:15:48Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:99: cfr_300.154_v2 10142 97ed29898220cd0e 2026-10-22T03:15:53Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:100: cfr_300.600_v2 2760 6e7d87ed6233ef2b 2026-10-22T03:15:54Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:101: cfr_229_v2 38 b1dc008cf1287a84 2026-10-22T03:20:46Z (eCFR versioner 2026-10-13, --compressed, HTTP 404; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:102: cfr_2_v2 38 b1dc008cf1287a84 2026-10-22T03:20:46Z (eCFR versioner 2026-10-13, --compressed, HTTP 404; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:103: cfr_300.229_v2 990 9117032dc8a9723e 2026-10-22T03:20:50Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:104: cfr_300.322_v2 2965 165ee80d52c34ee2 2026-10-22T03:21:30Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:105: cfr_300.531_v2 197 913c37302621b689 2026-10-22T03:24:38Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:106: cfr_300.532_v2 3202 d2b9ba22aca6f2b3 2026-10-22T03:24:38Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:107: cfr_300.533_v2 492 075bc32bb5e2ca18 2026-10-22T03:24:39Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:108: cfr_300.534_v2 3051 7d549ca645ff9e54 2026-10-22T03:24:39Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:109: cfr_300.168_v2 1660 59ce1b42a465b1ab 2026-10-22T03:26:37Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:110: cfr_300.302_v2 341 875116a52cf3545a 2026-10-22T03:32:37Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:111: cfr_300.623_v2 779 473b13697161e46f 2026-10-22T03:32:37Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:112: cfr_300.610_v2 391 3efddb5ccfd48255 2026-10-22T03:32:38Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:113: cfr_300.611_v2 700 81556c56fdefbd17 2026-10-22T03:32:42Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:114: cases/546bv.pdf 546 U.S. bound volume. Source URL https://www.supremecourt.gov/opinions/boundvolumes/546bv.pdf ; HTTP 200 (re-fetch 2026-10-22T03:38:03Z, final URL same) ; sha256 bf3511808d9e73e1cba9341dd900f76abeb977c5b326502f8dcb3502c7b8ad1f ; re-fetched bytes identical to the stored file (sha256 match). Text: cases/546bv.txt. Original capture time is recorded in Federal_Cases_official_2026-10-22.md; this line is an appended record (PA/IDA request 03:35Z).
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:115: cases/548bv.pdf 548 U.S. bound volume. Source URL https://www.supremecourt.gov/opinions/boundvolumes/548bv.pdf ; HTTP 200 (re-fetch 2026-10-22T03:38:04Z, final URL same) ; sha256 97798f74ea284e3cda87ef3707bd0be629799871e22e07be4b11957bc191841a ; re-fetched bytes identical to the stored file (sha256 match). Text: cases/548bv.txt. Appended record (PA/IDA request 03:35Z).
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:116: 2026-10-22T03:42:42Z ED/HHS NRG 2016 foster care (AGENCY GUIDANCE, NOT LAW) 200 application/pdf https://www.acf.hhs.gov/sites/default/files/documents/cb/ed_hhs_foster_care_guidance.pdf -> https://acf.gov/sites/default/files/documents/cb/ed_hhs_foster_care_guidance.pdf captured 2026-10-22T03:41:55Z sha256 a674eb1499ec415b645b7dd60ed3181acf02586940d552b2459bc1657652eb6d; ed.gov www and www2 copies HTTP 403
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:117: cfr_300.104_v2 420 bd8ec782c0829987 2026-10-22T03:43:46Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:118: 2026-10-22T03:46:22Z NOTE to row 19 (cfr_300.168, 2026-10-22T00:19:00Z): the recorded hash 826007e00cb4044c and size 2069 are the .xml (cfr_300.168.xml). The .txt is cfr_300.168.txt, 1681 bytes, sha256 cd4f40cb9ace3d88ef8f9b94b4baf1314db372860feb5f79dbf0228545a3a172. Current v2 files: cfr_300.168_v2.xml 2069 bytes, sha256 826007e0...afb06d (same bytes as the row-19 xml); cfr_300.168_v2.txt 1660 bytes, sha256 59ce1b42a465b1abde5ed29ed63976a2dacedf0016432b4b35ff3f3b7960d5b7 (row 109). Row 19 left as written.
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:119: cfr_part303_full 355307 44dfb11404bdbe9e 2026-10-22T03:47:05Z (eCFR versioner 2026-10-13, Part 303 full, --compressed, HTTP 200; xml sha256 eb532c96159a79ec8694943e2d45c91422ee7118fbcfaa856079f1535a70e969)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:120: cfr_300.613_v2 1373 d15efdb29c957aa4 2026-10-22T03:47:22Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:121: cfr_300.614_v2 431 5426f2c42e2e489c 2026-10-22T03:47:22Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:122: cfr_300.615_v2 314 5837641df6f3f17c 2026-10-22T03:47:22Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:123: cfr_300.616_v2 256 1a6dfc4f17574979 2026-10-22T03:47:23Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:124: cfr_300.617_v2 393 6289c04eb4ced2c0 2026-10-22T03:47:23Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:125: cfr_300.618_v2 738 34c5347519082820 2026-10-22T03:47:24Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:126: cfr_300.619_v2 312 cfbfb2c02099b29a 2026-10-22T03:47:24Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:127: cfr_300.620_v2 1105 37dbd65481ab4601 2026-10-22T03:47:24Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:128: cfr_300.621_v2 168 e9d3daad68a3d06e 2026-10-22T03:47:27Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:129: cfr_300.624_v2 563 1b17f2b762e7cf90 2026-10-22T03:47:28Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:130: cfr_300.625_v2 853 51d788dcefa2b5a8 2026-10-22T03:47:28Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:131: cfr_300.39_v2 2603 4da97ed9896021e6 2026-10-22T03:48:12Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
artifacts/federal/src/CFR_CAPTURE_LOG_GA39_56.txt:132: cfr_300.17_v2 595 59eb1d57d12edc80 2026-10-22T03:48:12Z (eCFR versioner 2026-10-13, --compressed, HTTP 200; UPDATE12)
```

### artifacts/federal/src/CAPTURE_LOG_guidance.txt

```
artifacts/federal/src/CAPTURE_LOG_guidance.txt:1: == NRG24 capture-log row (written 2026-10-22T04:24:28Z (2026-10-21 21:24 PDT)) ==
artifacts/federal/src/CAPTURE_LOG_guidance.txt:2: Key: NRG24. Label: AGENCY GUIDANCE, NOT LAW.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:3: Title (per file header line 4): Ensuring Educational Stability and Success for Students in Foster Care: Non-Regulatory Guidance (ED & HHS), Nov. 15, 2024.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:4: Official host URL (file header line 2): https://www.ed.gov/media/document/non-regulatory-guidance-ensuring-educational-stability-and-success-students-foster-care-november-15-2024-108448.pdf
artifacts/federal/src/CAPTURE_LOG_guidance.txt:5: Original capture: 2026-10-15 (file header line 6); PDF mtime 2026-10-15T21:10:31Z; 1359340 bytes.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:6:   PDF sha256 5bd22db3451aa830833f29218562a39e5059f5b3b7105f0627013d7960118bff (ED_HHS_Foster_Care_NRG_2024-11-15.pdf)
artifacts/federal/src/CAPTURE_LOG_guidance.txt:7:   TXT sha256 190042918c92c1701e97095f674f373d3cf23538a76520543d84c66cbcaf09f6 (ED_HHS_Foster_Care_NRG_2024-11-15.txt)
artifacts/federal/src/CAPTURE_LOG_guidance.txt:8:   PDF metadata (pdfinfo): Creator Acrobat PDFMaker 24 for Word; CreationDate 2024-11-14 16:29:30 UTC.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:9:   HTTP status of the 2026-10-15 fetch: NOT RECORDED at the time. UNRESOLVED.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:10: Re-fetch attempts from this computer for status: 2026-10-22T04:24:08Z HTTP 403 (11712 bytes, sha256 139f8843..., not the PDF); 2026-10-22T04:24:17Z with browser headers HTTP 403 (8059 bytes, sha256 71ffb968...). The host blocks scripted fetches now. The PDF on file could not be re-matched to the live host. Hash match to host: UNRESOLVED.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:11: 
artifacts/federal/src/CAPTURE_LOG_guidance.txt:12: == Captures appended 2026-10-22T04:35:11Z (2026-10-21 21:35 PDT) (IDA 04:24 item b, IDA 04:32 item 3) ==
artifacts/federal/src/CAPTURE_LOG_guidance.txt:13: CAP-1450 | 45 CFR 1356.60 Fiscal requirements (title IV-E) | REGULATION (RELATED FEDERAL BASELINE (outside IDEA)) | URL https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-45?part=1356&section=1356.60 | fetched 2026-10-22T04:34:02Z | HTTP 200 | HTML captures/ecfr_45cfr1356.60_20261022T043402Z.html sha256 7146e9e9fee3d5950b922fdbaf5d555c516153859255f048a7a279e1151fe9f5 (15800 bytes) | TXT (tags stripped) captures/ecfr_45cfr1356.60_20261022T043402Z.txt sha256 d3401ab656cc7b488b1f2e18d2916e18a00adb08ea86da60d93e29772f02398e, 37 lines; regulation text lines 1-35, amendment history line 36, JSON trailer line 37 | read in full. Keywords: transport 0, school 0, educat 1 (line 12, training at educational institutions). (c)(2) admin examples at lines 15-26; 50 percent rate at line 13.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:14: CAP-PI1011 | ACYF-CB-PI-10-11, Program Instruction, issued July 9, 2010 [PI1011:4] | AGENCY GUIDANCE, NOT LAW; RELATED FEDERAL BASELINE (outside IDEA) | URL https://acf.gov/sites/default/files/documents/cb/pi1011.pdf (the acf.hhs.gov URL redirects here) | first two tries 2026-10-22T04:34:13Z HTTP 202 empty body, not saved; retry 2026-10-22T04:34:28Z HTTP 200 application/pdf, headers in captures/ACYF-CB-PI-10-11_acf.gov_20261022T043428Z.headers.txt | PDF captures/ACYF-CB-PI-10-11_acf.gov_20261022T043428Z.pdf sha256 5ba6d7e9d939c942870ce8cfe7588c7207ef493a2ebcb879812fc4bdd7857f36 (727803 bytes, 55 pages, CreationDate 2012-03-21, ModDate 2012-05-19) | TXT pdftotext -layout sha256 330f97453fd47076b8b9a4c2881698f33e2477ab1a530a00ce946f4b7c964623, 2200 lines | read: lines 1-45, 860-989 (Section E), 1380-1434 (Section M); rest keyword-only (transport, school of origin, 1356.60, educational stability). School-of-origin transportation as allowable title IV-E administrative cost at lines 977-985, citing 45 CFR 1356.60(c)(2). NOTE: PDF dates postdate the July 2010 issuance; whether this file is a later revision is UNRESOLVED.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:15: CAP-YUD | OSEP Letter to Yudien, August 19, 2003 | AGENCY GUIDANCE, NOT LAW | NOT CAPTURED, UNRESOLVED. Tries: (1) https://sites.ed.gov/idea/idea-files/policy-letter-august-19-2003-to-vermont-department-of-education-legal-counsel-geoffrey-a-yudien/ at 2026-10-22T04:34:49Z HTTP 403 (block page kept as captures/Letter_to_Yudien_page_20261022T043449Z.html sha256 20c1042f6cba537e7d11a5efeb4134f19207226f0cbf4f102cd3e602efbf45b4, not the letter); (2) https://www2.ed.gov/policy/speced/guid/idea/letters/2003-3/yudien081903fape3q2003.pdf (URL as printed in DCL14 lines 241-242) at 2026-10-22T04:34:54Z HTTP 403; (3) a sites.ed.gov path I constructed from (2), same time, HTTP 403. Page URL (1) came from a web search result; search snippet text is not primary and is not used. Routed to IDA for browser re-fetch with NRG24.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:16: 
artifacts/federal/src/CAPTURE_LOG_guidance.txt:17: == Browser captures logged 2026-10-22T04:42:14Z (2026-10-21 21:42 PDT) (IDA 04:40; fetched by IDA through the box browser, not by IDEA Federal) ==
artifacts/federal/src/CAPTURE_LOG_guidance.txt:18: NRG24 host match | captures/browser/NRG24_browser.pdf | fetched by IDA from the ed.gov URL in the NRG24 row above, about 2026-10-22T04:36Z (time per IDA; HTTP status not recorded by me) | sha256 5bd22db3451aa830833f29218562a39e5059f5b3b7105f0627013d7960118bff, 1359340 bytes, computed by me at 2026-10-22T04:42:14Z | identical to the PDF on file (row above). Hash match to host: CONFIRMED. The earlier FLAG (hash match UNRESOLVED) is cleared. The 2026-10-15 HTTP status stays NOT RECORDED.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:19: CAP-YUD (supersedes NOT CAPTURED above) | OSEP Letter to Yudien | AGENCY GUIDANCE, NOT LAW | PDF captures/browser/Yudien_2003-08-19_browser.pdf from https://sites.ed.gov/idea/files/idea/policy/speced/guid/idea/letters/2003-3/yudien081903fape3q2003.pdf, about 2026-10-22T04:38Z (per IDA) | sha256 b2f965e9dcdaf704045fe23c2172c1f2b9e88348e19a3558ffcc49ae19a9e805 (122214 bytes; 3 pp; pdfinfo Creator Input Solutions, Inc., ModDate 2004-01-21, CreationDate blank) | TXT (pdftotext -layout, by me) captures/browser/Yudien_2003-08-19_browser.txt, 138 lines, sha256 9d98deef8a8502cb0c0101ed434ad9e83219179719bc6be1fd2818a25d44bf5c; read in full by me. P key YUD.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:20:   Date discrepancy: the text layer reads "AUG 19 2008" [YUD:7]; the host page title says August 19, 2003, the URL path has 2003-3, and the PDF ModDate is 2004-01-21. INFERENCE: 2008 is a text-layer misread of a 2003 date stamp. The page image is not re-read by me (UNRESOLVED as to the image).
artifacts/federal/src/CAPTURE_LOG_guidance.txt:21:   Text-layer errors noted: "300.31 l(c)(1)" [YUD:21] for 300.311(c)(1); "a flee" [YUD:33] for a free. The letter cites pre-2006 regulation numbers (300.311(c)(1), 300.122(a)(2), 300.300(a)); current counterparts are 300.324(d)(2)(i), 300.102(a)(2) and 300.101(a) (INFERENCE from matching text, not from a derivation table).
artifacts/federal/src/CAPTURE_LOG_guidance.txt:22: Yudien page | captures/browser/Yudien_page.html | sha256 61af200efcee471792626859b6046720362b29b65d5a1fbcbf980770de97fd58 (136352 bytes) | RENDERED DOM saved by the browser, NOT the original HTML source. Title: POLICY LETTER: August 19, 2003 to Vermont Department of Education Legal Counsel Geoffrey A. Yudien. The page also links a .doc version, not captured.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:23: 
artifacts/federal/src/CAPTURE_LOG_guidance.txt:24: == Appended 2026-10-22T04:43:59Z (2026-10-21 21:43 PDT) (IDA 04:43) ==
artifacts/federal/src/CAPTURE_LOG_guidance.txt:25: CAP-200306 | 2 CFR 200.306 Cost sharing (current eCFR) | REGULATION; RELATED FEDERAL BASELINE (outside IDEA) | fetched by me. Try 1 2026-10-22T04:43:30Z URL https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-2?part=200&section=200.306 HTTP 302, 0 bytes (files ecfr_2cfr200.306_20261022T044330Z.html/.txt are EMPTY, kept as record, not a capture). Try 2 2026-10-22T04:43:37Z following the redirect to https://www.ecfr.gov/api/renderer/v1/content/enhanced/current/title-2?subtitle=A&chapter=II&part=200&subpart=D&section=200.306 HTTP 200, 13897 bytes | HTML captures/ecfr_2cfr200.306_20261022T044337Z.html sha256 b35b5bab01094cb6126dc42c5f8a6cb0a404dbd884b4d291b4d3ce0d76c9a6b8 | TXT (tag-stripped by me) .txt sha256 fa4dc3b943a75d20af6206c96dd138693bb90151e0ecdc54379373c9944e1a20, 28 lines (line 28 is page JSON; source note 89 FR 30136, Apr. 22, 2024) | read in full (lines 1-27). P key C200306.
artifacts/federal/src/CAPTURE_LOG_guidance.txt:26: CAP-YUD IMAGE READING | page 1 of captures/browser/Yudien_2003-08-19_browser.pdf rendered by me with pdftoppm -r 150 to captures/browser/yud_p1-1.png (sha256 c83debfa56847e76103fd587445c0b5439267e40ce6a33913fc440b3d49b43ff); date area crop yud_p1_datecrop.png (sha256 675fea1381de61fa445efedb20853c090a233e4ec5466a498ced9457011ccde7), viewed by me | IMAGE READING: the date stamp shows AUG 19 2003. The text layer "AUG 19 2008" [YUD:7] is a text-layer error. This replaces the earlier INFERENCE (misread); the date is now read from the image, consistent with the host page title and URL path.
```

### artifacts/federal/src/official/rowley_458us176_provenance.txt

```
artifacts/federal/src/official/rowley_458us176_provenance.txt:1: File: rowley_458us176.pdf
artifacts/federal/src/official/rowley_458us176_provenance.txt:2: Source URL (verified: byte-identical download on 2026-10-15): https://tile.loc.gov/storage-services/service/ll/usrep/usrep458/usrep458176/usrep458176.pdf
artifacts/federal/src/official/rowley_458us176_provenance.txt:3: First page caption: Board of Education of the Hendrick Hudson Central School District, Westchester County, et al. v. Rowley, by her parents, Rowley et ux.; cert. to U.S. Court of Appeals for the Second Circuit; No. 80-1002; Argued Mar 23, 1982, Decided June 28, 1982 (October Term 1981, 458 U.S., Syllabus)
artifacts/federal/src/official/rowley_458us176_provenance.txt:4: Citation: 458 U.S. 176 (1982)
```

### artifacts/federal/src/official/honig_484us305_provenance.txt

```
artifacts/federal/src/official/honig_484us305_provenance.txt:1: File: honig_484us305.pdf
artifacts/federal/src/official/honig_484us305_provenance.txt:2: Source URL (verified: byte-identical download on 2026-10-15): https://tile.loc.gov/storage-services/service/ll/usrep/usrep484/usrep484305/usrep484305.pdf
artifacts/federal/src/official/honig_484us305_provenance.txt:3: First page caption: Honig, California Superintendent of Public Instruction v. Doe et al.; cert. to U.S. Court of Appeals for the Ninth Circuit; No. 86-728; Argued Nov 9, 1987, Decided Jan 20, 1988 (Syllabus)
artifacts/federal/src/official/honig_484us305_provenance.txt:4: Citation: 484 U.S. 305 (1988)
```

### artifacts/federal/src/official/endrew_f_15-827_provenance.txt

```
artifacts/federal/src/official/endrew_f_15-827_provenance.txt:1: File: endrew_f_15-827.pdf
artifacts/federal/src/official/endrew_f_15-827_provenance.txt:2: Source URL (verified: byte-identical download on 2026-10-15): https://www.supremecourt.gov/opinions/16pdf/15-827_0pm1.pdf
artifacts/federal/src/official/endrew_f_15-827_provenance.txt:3: First page caption: Endrew F., a minor, by and through his parents and next friends, Joseph F. et al. v. Douglas County School District RE-1; cert. to U.S. Court of Appeals for the Tenth Circuit; No. 15-827; Argued Jan 11, 2017, Decided Mar 22, 2017 (Slip Opinion, October Term 2016, Syllabus)
artifacts/federal/src/official/endrew_f_15-827_provenance.txt:4: Citation: 580 U.S. 386 (2017) [from memory; not shown on slip opinion page 1]
```

### artifacts/federal/src/official/fry_15-497_provenance.txt

```
artifacts/federal/src/official/fry_15-497_provenance.txt:1: File: fry_15-497.pdf
artifacts/federal/src/official/fry_15-497_provenance.txt:2: Source URL: NOT VERIFIED. Presumably supremecourt.gov/opinions/16pdf/15-497_*.pdf; the exact slug could not be confirmed (my guess 15-497_6k47.pdf returned 404). PDF metadata title: '15-497 Fry v. Napoleon Community Schools (02/22/2017)'.
artifacts/federal/src/official/fry_15-497_provenance.txt:3: First page caption: Fry et vir, as next friends of minor E. F. v. Napoleon Community Schools et al.; cert. to U.S. Court of Appeals for the Sixth Circuit; No. 15-497; Argued Oct 31, 2016, Decided Feb 22, 2017 (Slip Opinion, October Term 2016, Syllabus)
artifacts/federal/src/official/fry_15-497_provenance.txt:4: Citation: 580 U.S. 154 (2017) [from memory; not on slip page 1]
artifacts/federal/src/official/fry_15-497_provenance.txt:5: 
artifacts/federal/src/official/fry_15-497_provenance.txt:6: Appended correction 2026-10-21 21:26 UTC / 14:26 PDT: Source URL now VERIFIED. https://www.supremecourt.gov/opinions/16pdf/15-497_p8k0.pdf returned HTTP 200 at 2026-10-21T21:26:17Z; SHA-256 of the fresh download equals this file (f6fd0434d4c0d4f6c5a7a2f3ab85e87733d97ff0646372ba87b21eb7efa169ee). 26 pages. The 580 U.S. 154 citation above remains from memory and is not verified.
```

## Appendix D. IDEA Federal lines in the project status file (status.md at the project root)

```
status.md:13: - 2026-10-15 21:06 UTC IDEA Federal: Federal_Required_Artifacts_Checklist.md (+ .csv) saved in artifacts/federal/; 4 guidance docs unverified in full (see Part C).
status.md:48: - 2026-10-15 21:26 UTC / 13:26 PST | IDEA Federal | correction read and applied: no workers used from now (running helper stopped); all prior items incl. checklist, log, errata reclassified UNVERIFIED; Cornell LII and snippet-based items BLOCKED pending official source; check-in written with corrections section; my own full re-reads still to do
status.md:55: - 2026-10-15 21:53 UTC / 13:53 PST | IDEA Federal | own full reads logged: 300.519, 300.503, 300.324, 300.102 (eCFR captures) and OSEP 2014 letter (ed.gov capture); errata 300.324(c)/(d) and 300.102(a)(2) now match on my read; remaining captures, DC HOD, ED/DOJ principles, ED/HHS 2024 guidance, official USC and case texts still to read
status.md:138: 2026-10-15 23:52 UTC (16:52 PDT) IDEA Federal: captured and read 300.2 and 300.28; posted Federal_Provision_List.md/.csv (13 rows READ, rest not yet read or UNRESOLVED) and NV first-pass counterpart checks. No workers used.
status.md:166: 2026-10-15 23:59 UTC (16:59 PDT) IDEA Federal: GA, UT, DC counterpart checks posted (Federal_Counterpart_Checks_GA_UT_DC.md); NV note updated after reading 300.301(c) and 300.320(c).
```
