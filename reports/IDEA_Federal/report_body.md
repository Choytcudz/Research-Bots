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
