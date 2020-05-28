# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Features

            #### Petitioner/Respondent 

                1	Attorney general of the United States, or his office
                2	Specified state board or department of education
                3	City, town, township, village, or borough government or governmental unit
                4	State commission, board, committee, or authority
                5	County government or county governmental unit, except school district
                6	Court or judicial district
                7	State department or agency
                8	Governmental employee or job applicant
                9	Female governmental employee or job applicant
                10	Minority governmental employee or job applicant
                11	Minority female governmental employee or job applicant
                12	Not listed among agencies in the first Administrative Action variable
                13	Retired or former governmental employee
                14	U.S. House of Representatives
                15	Interstate compact
                16	Judge
                17	State legislature, house, or committee
                18	Local governmental unit other than a county, city, town, township, village, or borough
                19	Governmental official, or an official of an agency established under an interstate compact
                20	State or U.S. supreme court
                21	Local school district or board of education
                22	U.S. Senate
                23	U.S. senator
                24	Foreign nation or instrumentality
                25	State or local governmental taxpayer, or executor of the estate of
                26	State college or university
                27	United States
                28	State
                100	Person accused, indicted, or suspected of crime
                101	Advertising business or agency
                102	Agent, fiduciary, trustee, or executor
                103	Airplane manufacturer, or manufacturer of parts of airplanes
                104	Airline
                105	Distributor, importer, or exporter of alcoholic beverages
                106	Alien, person subject to a denaturalization proceeding, or one whose citizenship is revoked
                107	American Medical Association
                108	National Railroad Passenger Corp.
                109	A establishment, or recreational facility
                110	Arrested person, or pretrial detainee
                111	Attorney, or person acting as such;includes bar applicant or law student, or law firm or bar association
                112	Author, copyright holder
                113	Bank, savings and loan, credit union, investment company
                114	Bankrupt person or business, or business in reorganization
                115	Establishment serving liquor by the glass, or package liquor store
                116	Water transportation, stevedore
                117	Bookstore, newsstand, printer, bindery, purveyor or distributor of books or magazines
                118	Brewery, distillery
                119	Broker, stock exchange, investment or securities firm
                120	Construction industry
                121	Bus or motorized passenger transportation vehicle
                122	Business, corporation
                123	Buyer, purchaser
                124	Cable TV
                125	Car dealer
                126	Person convicted of crime
                127	Tangible property, other than real estate, including contraband
                128	Chemical company
                129	Child, children, including adopted or illegitimate
                130	Religious organization, institution, or person
                131	Private club or facility
                132	Coal company or coal mine operator
                133	Computer business or manufacturer, hardware or software
                134	Consumer, consumer organization
                135	Creditor, including institution appearing as such; e.g., a finance company
                136	Person allegedly criminally insane or mentally incompetent to stand trial
                137	Defendant
                138	Debtor
                139	Real estate developer
                140	Disabled person or disability benefit claimant
                141	Distributor
                142	Person subject to selective service, including conscientious objector
                143	Drug manufacturer
                144	Druggist, pharmacist, pharmacy
                145	Employee, or job applicant, including beneficiaries of
                146	Employer-employee trust agreement, employee health and welfare fund, or multi-employer pension plan
                147	Electric equipment manufacturer
                148	Electric or hydroelectric power utility, power cooperative, or gas and electric company
                149	Eleemosynary institution or person
                150	Environmental organization
                151	Employer. If employer's relations with employees are governed by the nature of the employer's business (e.g., railroad, boat), rather than labor law generally, the more specific designation is used in place of Employer.
                152	Farmer, farm worker, or farm organization
                153	Father
                154	Female employee or job applicant
                155	Female
                156	Movie, play, pictorial representation, theatrical production, actor, or exhibitor or distributor of
                157	Fisherman or fishing company
                158	Food, meat packing, or processing company, stockyard
                159	Foreign (non-American) nongovernmental entity
                160	Franchiser
                161	Franchisee
                162	Lesbian, gay, bisexual, transexual person or organization
                163	Person who guarantees another's obligations
                164	Handicapped individual, or organization of devoted to
                165	Health organization or person, nursing home, medical clinic or laboratory, chiropractor
                166	Heir, or beneficiary, or person so claiming to be
                167	Hospital, medical center
                168	Husband, or ex-husband
                169	Involuntarily committed mental patient
                170	Indian, including Indian tribe or nation
                171	Insurance company, or surety
                172	Inventor, patent assigner, trademark owner or holder
                173	Investor
                174	Injured person or legal entity, nonphysically and non-employment related
                175	Juvenile
                176	Government contractor
                177	Holder of a license or permit, or applicant therefor
                178	Magazine
                179	Male
                180	Medical or Medicaid claimant
                181	Medical supply or manufacturing co.
                182	Racial or ethnic minority employee or job applicant
                183	Minority female employee or job applicant
                184	Manufacturer
                185	Management, executive officer, or director, of business entity
                186	Military personnel, or dependent of, including reservist
                187	Mining company or miner, excluding coal, oil, or pipeline company
                188	Mother
                189	Auto manufacturer
                190	Newspaper, newsletter, journal of opinion, news service
                191	Radio and television network, except cable tv
                192	Nonprofit organization or business
                193	Nonresident
                194	Nuclear power plant or facility
                195	Owner, landlord, or claimant to ownership, fee interest, or possession of land as well as chattels
                196	Shareholders to whom a tender offer is made
                197	Tender offer
                198	Oil company, or natural gas producer
                199	Elderly person, or organization dedicated to the elderly
                200	Out of state noncriminal defendant
                201	Political action committee
                202	Parent or parents
                203	Parking lot or service
                204	Patient of a health professional
                205	Telephone, telecommunications, or telegraph company
                206	Physician, MD or DO, dentist, or medical society
                207	Public interest organization
                208	Physically injured person, including wrongful death, who is not an employee
                209	Pipe line company
                210	Package, luggage, container
                211	Political candidate, activist, committee, party, party member, organization, or elected official
                212	Indigent, needy, welfare recipient
                213	Indigent defendant
                214	Private person
                215	Prisoner, inmate of penal institution
                216	Professional organization, business, or person
                217	Probationer, or parolee
                218	Protester, demonstrator, picketer or pamphleteer (non-employment related), or non-indigent loiterer
                219	Public utility
                220	Publisher, publishing company
                221	Rio station
                222	Racial or ethnic minority
                223	Person or organization protesting racial or ethnic segregation or discrimination
                224	Racial or ethnic minority student or applicant for admission to an educational institution
                225	Realtor
                226	Journalist, columnist, member of the news media
                227	Resident
                228	Restaurant, food vendor
                229	Retarded person, or mental incompetent
                230	Retired or former employee
                231	Railroad
                232	Private school, college, or university
                233	Seller or vendor
                234	Shipper, including importer and exporter
                235	Shopping center, mall
                236	Spouse, or former spouse
                237	Stockholder, shareholder, or bondholder
                238	Retail business or outlet
                239	Student, or applicant for admission to an educational institution
                240	Taxpayer or executor of taxpayer's estate, federal only
                241	Tenant or lessee
                242	Theater, studio
                243	Forest products, lumber, or logging company
                244	Person traveling or wishing to travel abroad, or overseas travel agent
                245	Trucking company, or motor carrier
                246	Television station
                247	Union member
                248	Unemployed person or unemployment compensation applicant or claimant
                249	Union, labor organization, or official of
                250	Veteran
                251	Voter, prospective voter, elector, or a nonelective official seeking reapportionment or redistricting of legislative districts (POL)
                252	Wholesale trade
                253	Wife, or ex-wife
                254	Witness, or person under subpoena
                255	Network
                256	Slave
                257	Slave-owner
                258	Bank of the united states
                259	Timber company
                260	U.S. job applicants or employees
                301	Army and Air Force Exchange Service
                302	Atomic Energy Commission
                303	Secretary or administrative unit or personnel of the U.S. Air Force
                304	Department or Secretary of Agriculture
                305	Alien Property Custodian
                306	Secretary or administrative unit or personnel of the U.S. Army
                307	Board of Immigration Appeals
                308	Bureau of Indian Affairs
                310	Bonneville Power Administration
                311	Benefits Review Board
                312	Civil Aeronautics Board
                313	Bureau of the Census
                314	Central Intelligence Agency
                315	Commodity Futures Trading Commission
                316	Department or Secretary of Commerce
                317	Comptroller of Currency
                318	Consumer Product Safety Commission
                319	Civil Rights Commission
                320	Civil Service Commission, U.S.
                321	Customs Service or Commissioner of Customs
                322	Defense Base Closure and REalignment Commission
                323	Drug Enforcement Agency
                324	Department or Secretary of Defense (and Department or Secretary of War)
                325	Department or Secretary of Energy
                326	Department or Secretary of the Interior
                327	Department of Justice or Attorney General
                328	Department or Secretary of State
                329	Department or Secretary of Transportation
                330	Department or Secretary of Education
                331	U.S. Employees' Compensation Commission, or Commissioner
                332	Equal Employment Opportunity Commission
                333	Environmental Protection Agency or Administrator
                334	Federal Aviation Agency or Administration
                335	Federal Bureau of Investigation or Director
                336	Federal Bureau of Prisons
                337	Farm Credit Administration
                338	Federal Communications Commission (including a predecessor, Federal Radio Commission)
                339	Federal Credit Union Administration
                340	Food and Drug Administration
                341	Federal Deposit Insurance Corporation
                342	Federal Energy Administration
                343	Federal Election Commission
                344	Federal Energy Regulatory Commission
                345	Federal Housing Administration
                346	Federal Home Loan Bank Board
                347	Federal Labor Relations Authority
                348	Federal Maritime Board
                349	Federal Maritime Commission
                350	Farmers Home Administration
                351	Federal Parole Board
                352	Federal Power Commission
                353	Federal Railroad Administration
                354	Federal Reserve Board of Governors
                355	Federal Reserve System
                356	Federal Savings and Loan Insurance Corporation
                357	Federal Trade Commission
                358	Federal Works Administration, or Administrator
                359	General Accounting Office
                360	Comptroller General
                361	General Services Administration
                362	Department or Secretary of Health, Education and Welfare
                363	Department or Secretary of Health and Human Services
                364	Department or Secretary of Housing and Urban Development
                366	Interstate Commerce Commission
                367	Indian Claims Commission
                368	Immigration and Naturalization Service, or Director of, or District Director of, or Immigration and Naturalization Enforcement
                369	Internal Revenue Service, Collector, Commissioner, or District Director of
                370	Information Security Oversight Office
                371	Department or Secretary of Labor
                372	Loyalty Review Board
                373	Legal Services Corporation
                374	Merit Systems Protection Board
                375	Multistate Tax Commission
                376	National Aeronautics and Space Administration
                377	Secretary or administrative unit of the U.S. Navy
                378	National Credit Union Administration
                379	National Endowment for the Arts
                380	National Enforcement Commission
                381	National Highway Traffic Safety Administration
                382	National Labor Relations Board, or regional office or officer
                383	National Mediation Board
                384	National Railroad Adjustment Board
                385	Nuclear Regulatory Commission
                386	National Security Agency
                387	Office of Economic Opportunity
                388	Office of Management and Budget
                389	Office of Price Administration, or Price Administrator
                390	Office of Personnel Management
                391	Occupational Safety and Health Administration
                392	Occupational Safety and Health Review Commission
                393	Office of Workers' Compensation Programs
                394	Patent Office, or Commissioner of, or Board of Appeals of
                395	Pay Board (established under the Economic Stabilization Act of 1970)
                396	Pension Benefit Guaranty Corporation
                397	U.S. Public Health Service
                398	Postal Rate Commission
                399	Provider Reimbursement Review Board
                400	Renegotiation Board
                401	Railroad Adjustment Board
                402	Railroad Retirement Board
                403	Subversive Activities Control Board
                404	Small Business Administration
                405	Securities and Exchange Commission
                406	Social Security Administration or Commissioner
                407	Selective Service System
                408	Department or Secretary of the Treasury
                409	Tennessee Valley Authority
                410	United States Forest Service
                411	United States Parole Commission
                412	Postal Service and Post Office, or Postmaster General, or Postmaster
                413	United States Sentencing Commission
                414	Veterans' Administration
                415	War Production Board
                416	Wage Stabilization Board
                417	General Land Office of Commissioners
                418	Transportation Security Administration
                419	Surface Transportation Board
                420	U.S. Shipping Board Emergency Fleet Corp.
                421	Reconstruction Finance Corp.
                422	Department or Secretary of Homeland Security
                501	Unidentifiable
                600	International Entity

            #### Case Source/Original Court

                1	U.S. Court of Customs and Patent Appeals
                2	U.S. Court of International Trade
                3	U.S. Court of Claims, Court of Federal Claims
                4	U.S. Court of Military Appeals, renamed as Court of Appeals for the Armed Forces
                5	U.S. Court of Military Review
                6	U.S. Court of Veterans Appeals
                7	U.S. Customs Court
                8	U.S. Court of Appeals, Federal Circuit
                9	U.S. Tax Court
                10	Temporary Emergency U.S. Court of Appeals
                12	U.S. Court for China
                13	U.S. Consular Courts
                14	U.S. Commerce Court
                15	Territorial Supreme Court
                16	Territorial Appellate Court
                17	Territorial Trial Court
                18	Emergency Court of Appeals
                19	Supreme Court of the District of Columbia
                20	Bankruptcy Court
                21	U.S. Court of Appeals, First Circuit
                22	U.S. Court of Appeals, Second Circuit
                23	U.S. Court of Appeals, Third Circuit
                24	U.S. Court of Appeals, Fourth Circuit
                25	U.S. Court of Appeals, Fifth Circuit
                26	U.S. Court of Appeals, Sixth Circuit
                27	U.S. Court of Appeals, Seventh Circuit
                28	U.S. Court of Appeals, Eighth Circuit
                29	U.S. Court of Appeals, Ninth Circuit
                30	U.S. Court of Appeals, Tenth Circuit
                31	U.S. Court of Appeals, Eleventh Circuit
                32	U.S. Court of Appeals, District of Columbia Circuit (includes the Court of Appeals for the District of Columbia but not the District of Columbia Court of Appeals, which has local jurisdiction)
                41	Alabama Middle U.S. District Court
                42	Alabama Northern U.S. District Court
                43	Alabama Southern U.S. District Court
                44	Alaska U.S. District Court
                45	Arizona U.S. District Court
                46	Arkansas Eastern U.S. District Court
                47	Arkansas Western U.S. District Court
                48	California Central U.S. District Court
                49	California Eastern U.S. District Court
                50	California Northern U.S. District Court
                51	California Southern U.S. District Court
                52	Colorado U.S. District Court
                53	Connecticut U.S. District Court
                54	Delaware U.S. District Court
                55	District Of Columbia U.S. District Court
                56	Florida Middle U.S. District Court
                57	Florida Northern U.S. District Court
                58	Florida Southern U.S. District Court
                59	Georgia Middle U.S. District Court
                60	Georgia Northern U.S. District Court
                61	Georgia Southern U.S. District Court
                62	Guam U.S. District Court
                63	Hawaii U.S. District Court
                64	Idaho U.S. District Court
                65	Illinois Central U.S. District Court
                66	Illinois Northern U.S. District Court
                67	Illinois Southern U.S. District Court
                68	Indiana Northern U.S. District Court
                69	Indiana Southern U.S. District Court
                70	Iowa Northern U.S. District Court
                71	Iowa Southern U.S. District Court
                72	Kansas U.S. District Court
                73	Kentucky Eastern U.S. District Court
                74	Kentucky Western U.S. District Court
                75	Louisiana Eastern U.S. District Court
                76	Louisiana Middle U.S. District Court
                77	Louisiana Western U.S. District Court
                78	Maine U.S. District Court
                79	Maryland U.S. District Court
                80	Massachusetts U.S. District Court
                81	Michigan Eastern U.S. District Court
                82	Michigan Western U.S. District Court
                83	Minnesota U.S. District Court
                84	Mississippi Northern U.S. District Court
                85	Mississippi Southern U.S. District Court
                86	Missouri Eastern U.S. District Court
                87	Missouri Western U.S. District Court
                88	Montana U.S. District Court
                89	Nebraska U.S. District Court
                90	Nevada U.S. District Court
                91	New Hampshire U.S. District Court
                92	New Jersey U.S. District Court
                93	New Mexico U.S. District Court
                94	New York Eastern U.S. District Court
                95	New York Northern U.S. District Court
                96	New York Southern U.S. District Court
                97	New York Western U.S. District Court
                98	North Carolina Eastern U.S. District Court
                99	North Carolina Middle U.S. District Court
                100	North Carolina Western U.S. District Court
                101	North Dakota U.S. District Court
                102	Northern Mariana Islands U.S. District Court
                103	Ohio Northern U.S. District Court
                104	Ohio Southern U.S. District Court
                105	Oklahoma Eastern U.S. District Court
                106	Oklahoma Northern U.S. District Court
                107	Oklahoma Western U.S. District Court
                108	Oregon U.S. District Court
                109	Pennsylvania Eastern U.S. District Court
                110	Pennsylvania Middle U.S. District Court
                111	Pennsylvania Western U.S. District Court
                112	Puerto Rico U.S. District Court
                113	Rhode Island U.S. District Court
                114	South Carolina U.S. District Court
                115	South Dakota U.S. District Court
                116	Tennessee Eastern U.S. District Court
                117	Tennessee Middle U.S. District Court
                118	Tennessee Western U.S. District Court
                119	Texas Eastern U.S. District Court
                120	Texas Northern U.S. District Court
                121	Texas Southern U.S. District Court
                122	Texas Western U.S. District Court
                123	Utah U.S. District Court
                124	Vermont U.S. District Court
                125	Virgin Islands U.S. District Court
                126	Virginia Eastern U.S. District Court
                127	Virginia Western U.S. District Court
                128	Washington Eastern U.S. District Court
                129	Washington Western U.S. District Court
                130	West Virginia Northern U.S. District Court
                131	West Virginia Southern U.S. District Court
                132	Wisconsin Eastern U.S. District Court
                133	Wisconsin Western U.S. District Court
                134	Wyoming U.S. District Court
                150	Louisiana U.S. District Court
                151	Washington U.S. District Court
                152	West Virginia U.S. District Court
                153	Illinois Eastern U.S. District Court
                155	South Carolina Eastern U.S. District Court
                160	South Carolina Western U.S. District Court
                162	Alabama U.S. District Court
                163	U.S. District Court for the Canal Zone
                164	Georgia U.S. District Court
                165	Illinois U.S. District Court
                166	Indiana U.S. District Court
                167	Iowa U.S. District Court
                168	Michigan U.S. District Court
                169	Mississippi U.S. District Court
                170	Missouri U.S. District Court
                171	New Jersey Eastern U.S. District Court (East Jersey U.S. District Court)
                172	New Jersey Western U.S. District Court (West Jersey U.S. District Court)
                173	New York U.S. District Court
                174	North Carolina U.S. District Court
                175	Ohio U.S. District Court
                176	Pennsylvania U.S. District Court
                177	Tennessee U.S. District Court
                178	Texas U.S. District Court
                179	Virginia U.S. District Court
                180	Norfolk U.S. District Court
                181	Wisconsin U.S. District Court
                182	Kentucky U.S. Distrcrict Court
                183	New Jersey U.S. District Court
                184	California U.S. District Court
                185	Florida U.S. District Court
                186	Arkansas U.S. District Court
                187	District of Orleans U.S. District Court
                300	State Supreme Court
                301	State Appellate Court
                302	State Trial Court
                400	Eastern Circuit (of the United States)
                401	Middle Circuit (of the United States)
                402	Southern Circuit (of the United States)
                403	Alabama U.S. Circuit Court for (all) District(s) of Alabama
                404	Arkansas U.S. Circuit Court for (all) District(s) of Arkansas
                405	California U.S. Circuit for (all) District(s) of California
                406	Connecticut U.S. Circuit for the District of Connecticut
                407	Delaware U.S. Circuit for the District of Delaware
                408	Florida U.S. Circuit for (all) District(s) of Florida
                409	Georgia U.S. Circuit for (all) District(s) of Georgia
                410	Illinois U.S. Circuit for (all) District(s) of Illinois
                411	Indiana U.S. Circuit for (all) District(s) of Indiana
                412	Iowa U.S. Circuit for (all) District(s) of Iowa
                413	Kansas U.S. Circuit for the District of Kansas
                414	Kentucky U.S. Circuit for (all) District(s) of Kentucky
                415	Louisiana U.S. Circuit for (all) District(s) of Louisiana
                416	Maine U.S. Circuit for the District of Maine
                417	Maryland U.S. Circuit for the District of Maryland
                418	Massachusetts U.S. Circuit for the District of Massachusetts
                419	Michigan U.S. Circuit for (all) District(s) of Michigan
                420	Minnesota U.S. Circuit for the District of Minnesota
                421	Mississippi U.S. Circuit for (all) District(s) of Mississippi
                422	Missouri U.S. Circuit for (all) District(s) of Missouri
                423	Nevada U.S. Circuit for the District of Nevada
                424	New Hampshire U.S. Circuit for the District of New Hampshire
                425	New Jersey U.S. Circuit for (all) District(s) of New Jersey
                426	New York U.S. Circuit for (all) District(s) of New York
                427	North Carolina U.S. Circuit for (all) District(s) of North Carolina
                428	Ohio U.S. Circuit for (all) District(s) of Ohio
                429	Oregon U.S. Circuit for the District of Oregon
                430	Pennsylvania U.S. Circuit for (all) District(s) of Pennsylvania
                431	Rhode Island U.S. Circuit for the District of Rhode Island
                432	South Carolina U.S. Circuit for the District of South Carolina
                433	Tennessee U.S. Circuit for (all) District(s) of Tennessee
                434	Texas U.S. Circuit for (all) District(s) of Texas
                435	Vermont U.S. Circuit for the District of Vermont
                436	Virginia U.S. Circuit for (all) District(s) of Virginia
                437	West Virginia U.S. Circuit for (all) District(s) of West Virginia
                438	Wisconsin U.S. Circuit for (all) District(s) of Wisconsin
                439	Wyoming U.S. Circuit for the District of Wyoming
                440	Circuit Court of the District of Columbia
                441	Nebraska U.S. Circuit for the District of Nebraska
                442	Colorado U.S. Circuit for the District of Colorado
                443	Washington U.S. Circuit for (all) District(s) of Washington
                444	Idaho U.S. Circuit Court for (all) District(s) of Idaho
                445	Montana U.S. Circuit Court for (all) District(s) of Montana
                446	Utah U.S. Circuit Court for (all) District(s) of Utah
                447	South Dakota U.S. Circuit Court for (all) District(s) of South Dakota
                448	North Dakota U.S. Circuit Court for (all) District(s) of North Dakota
                449	Oklahoma U.S. Circuit Court for (all) District(s) of Oklahoma
                601	Court of Private Land Claims

            #### Specific Issue

                10010	Involuntary confession
                10020	Habeas corpus
                10030	Plea bargaining: the constitutionality of and/or the circumstances of its exercise
                10040	Retroactivity (of newly announced or newly enacted constitutional or statutory rights)
                10050	Search and seizure (other than as pertains to vehicles or Crime Control Act)
                10060	Search and seizure, vehicles
                10070	Search and seizure, Crime Control Act
                10080	Contempt of court or congress
                10090	Self-incrimination (other than as pertains to Miranda or immunity from prosecution)
                10100	Miranda warnings
                10110	Self-incrimination, immunity from prosecution
                10120	Right to counsel (cf. indigents appointment of counsel or inadequate representation)
                10130	Cruel and unusual punishment, death penalty (cf. extra legal jury influence, death penalty)
                10140	Cruel and unusual punishment, non-death penalty (cf. liability, civil rights acts)
                10150	Line-up
                10160	Discovery and inspection (in the context of criminal litigation only, otherwise Freedom of Information Act and related federal or state statutes or regulations)
                10170	Ddouble jeopardy
                10180	Ex post facto (state)
                10190	Extra-legal jury influences: miscellaneous
                10200	Extra-legal jury influences: prejudicial statements or evidence
                10210	Extra-legal jury influences: contact with jurors outside courtroom
                10220	Extra-legal jury influences: jury instructions (not necessarily in criminal cases)
                10230	Extra-legal jury influences: voir dire (not necessarily a criminal case)
                10240	Extra-legal jury influences: prison garb or appearance
                10250	Extra-legal jury influences: jurors and death penalty (cf. cruel and unusual punishment)
                10260	Extra-legal jury influences: pretrial publicity
                10270	Confrontation (right to confront accuser, call and cross-examine witnesses)
                10280	Subconstitutional fair procedure: confession of error
                10290	Subconstitutional fair procedure: conspiracy (cf. Federal Rules of Criminal Procedure: conspiracy)
                10300	Subconstitutional fair procedure: entrapment
                10310	Subconstitutional fair procedure: exhaustion of remedies
                10320	Subconstitutional fair procedure: fugitive from justice
                10330	Subconstitutional fair procedure: presentation, admissibility, or sufficiency of evidence (not necessarily a criminal case)
                10340	Subconstitutional fair procedure: stay of execution
                10350	Subconstitutional fair procedure: timeliness
                10360	Subconstitutional fair procedure: miscellaneous
                10370	Federal Rules of Criminal Procedure
                10380	Statutory construction of criminal laws: assault
                10390	Statutory construction of criminal laws: bank robbery
                10400	Statutory construction of criminal laws: conspiracy (cf. subconstitutional fair procedure: conspiracy)
                10410	Statutory construction of criminal laws: escape from custody
                10420	Statutory construction of criminal laws: false statements (cf. statutory construction of criminal laws: perjury)
                10430	Statutory construction of criminal laws: financial (other than in fraud or internal revenue)
                10440	Statutory construction of criminal laws: firearms
                10450	Statutory construction of criminal laws: fraud
                10460	Statutory construction of criminal laws: gambling
                10470	Statutory construction of criminal laws: Hobbs Act; i.e., 18 USC 1951
                10480	Statutory construction of criminal laws: immigration (cf. immigration and naturalization)
                10490	Statutory construction of criminal laws: internal revenue (cf. Federal Taxation)
                10500	Statutory construction of criminal laws: Mann Act and related statutes
                10510	Statutory construction of criminal laws: narcotics includes regulation and prohibition of alcohol
                10520	Statutory construction of criminal laws: obstruction of justice
                10530	Statutory construction of criminal laws: perjury (other than as pertains to statutory construction of criminal laws: false statements)
                10540	Statutory construction of criminal laws: Travel Act, 18 USC 1952
                10550	Statutory construction of criminal laws: war crimes
                10560	Statutory construction of criminal laws: sentencing guidelines
                10570	Statutory construction of criminal laws: miscellaneous
                10580	Jury trial (right to, as distinct from extra-legal jury influences)
                10590	Speedy trial
                10600	Miscellaneous criminal procedure (cf. due process, prisoners' rights, comity: criminal procedure)
                20010	Voting
                20020	Voting Rights Act of 1965, plus amendments
                20030	Ballot access (of candidates and political parties)
                20040	Desegregation (other than as pertains to school desegregation, employment discrimination, and affirmative action)
                20050	Desegregation, schools
                20060	Employment discrimination: on basis of race, age, religion, illegitimacy, national origin, or working conditions.
                20070	Affirmative action
                20075	Slavery or indenture
                20080	Sit-in demonstrations (protests against racial discrimination in places of public accommodation)
                20090	Reapportionment: other than plans governed by the Voting Rights Act
                20100	Debtors' rights
                20110	Deportation (cf. immigration and naturalization)
                20120	Employability of aliens (cf. immigration and naturalization)
                20130	Sex discrimination (excluding sex discrimination in employment)
                20140	Sex discrimination in employment (cf. sex discrimination)
                20150	Indians (other than pertains to state jurisdiction over)
                20160	Indians, state jurisdiction over
                20170	Juveniles (cf. rights of illegitimates)
                20180	Poverty law, constitutional
                20190	Poverty law, statutory: welfare benefits, typically under some Social Security Act provision.
                20200	Illegitimates, rights of (cf. juveniles): typically inheritance and survivor's benefits, and paternity suits
                20210	Handicapped, rights of: under Rehabilitation, Americans with Disabilities Act, and related statutes
                20220	Residency requirements: durational, plus discrimination against nonresidents
                20230	Military: draftee, or person subject to induction
                20240	Military: active duty
                20250	Military: veteran
                20260	Immigration and naturalization: permanent residence
                20270	Immigration and naturalization: citizenship
                20280	Immigration and naturalization: loss of citizenship, denaturalization
                20290	Immigration and naturalization: access to public education
                20300	Immigration and naturalization: welfare benefits
                20310	Immigration and naturalization: miscellaneous
                20320	Indigents: appointment of counsel (cf. right to counsel)
                20330	Indigents: inadequate representation by counsel (cf. right to counsel)
                20340	Indigents: payment of fine
                20350	Indigents: costs or filing fees
                20360	Indigents: U.S. Supreme Court docketing fee
                20370	Indigents: transcript
                20380	Indigents: assistance of psychiatrist
                20390	Indigents: miscellaneous
                20400	Liability, civil rights acts (cf. liability, governmental and liability, nongovernmental; cruel and unusual punishment, non-death penalty)
                20410	Miscellaneous civil rights (cf. comity: civil rights)
                30010	First Amendment, miscellaneous (cf. comity: First Amendment)
                30020	Commercial speech, excluding attorneys
                30030	Libel, defamation: defamation of public officials and public and private persons
                30040	Libel, privacy: true and false light invasions of privacy
                30050	Legislative investigations: concerning internal security only
                30060	Federal or state internal security legislation: Smith, Internal Security, and related federal statutes
                30070	Loyalty oath or non-Communist affidavit (other than bar applicants, government employees, political party, or teacher)
                30080	Loyalty oath: bar applicants (cf. admission to bar, state or federal or U.S. Supreme Court)
                30090	Loyalty oath: government employees
                30100	Loyalty oath: political party
                30110	Loyalty oath: teachers
                30120	Security risks: denial of benefits or dismissal of employees for reasons other than failure to meet loyalty oath requirements
                30130	Conscientious objectors (cf. military draftee or military active duty) to military service
                30140	Campaign spending (cf. governmental corruption):
                30150	Protest demonstrations (other than as pertains to sit-in demonstrations): demonstrations and other forms of protest based on First Amendment guarantees
                30160	Free exercise of religion
                30170	Establishment of religion (other than as pertains to parochiaid:)
                30180	Parochiaid: government aid to religious schools, or religious requirements in public schools
                30190	Obscenity, state (cf. comity: privacy): including the regulation of sexually explicit material under the 21st Amendment
                30200	Obscenity, federal
                40010	Due process: miscellaneous (cf. loyalty oath), the residual code
                40020	Due process: hearing or notice (other than as pertains to government employees or prisoners' rights)
                40030	Due process: hearing, government employees
                40040	Due process: prisoners' rights and defendants' rights
                40050	Due process: impartial decision maker
                40060	Due process: jurisdiction (jurisdiction over non-resident litigants)
                40070	Due process: takings clause, or other non-constitutional governmental taking of property
                50010	Privacy (cf. libel, comity: privacy)
                50020	Abortion: including contraceptives
                50030	Right to die
                50040	Freedom of Information Act and related federal or state statutes or regulations
                60010	Attorneys' and governmental employees' or officials' fees or compensation or licenses
                60020	Commercial speech, attorneys (cf. commercial speech)
                60030	Admission to a state or federal bar, disbarment, and attorney discipline (cf. loyalty oath: bar applicants)
                60040	Admission to, or disbarment from, Bar of the U.S. Supreme Court
                70010	Arbitration (in the context of labor-management or employer-employee relations) (cf. arbitration)
                70020	Union antitrust: legality of anticompetitive union activity
                70030	Union or closed shop: includes agency shop litigation
                70040	Fair Labor Standards Act
                70050	Occupational Safety and Health Act
                70060	Union-union member dispute (except as pertains to union or closed shop)
                70070	Labor-management disputes: bargaining
                70080	Labor-management disputes: employee discharge
                70090	Labor-management disputes: distribution of union literature
                70100	Labor-management disputes: representative election
                70110	Labor-management disputes: antistrike injunction
                70120	Labor-management disputes: jurisdictional dispute
                70130	Labor-management disputes: right to organize
                70140	Labor-management disputes: picketing
                70150	Labor-management disputes: secondary activity
                70160	Labor-management disputes: no-strike clause
                70170	Labor-management disputes: union representatives
                70180	Labor-management disputes: union trust funds (cf. ERISA)
                70190	Labor-management disputes: working conditions
                70200	Labor-management disputes: miscellaneous dispute
                70210	Miscellaneous union
                80010	Antitrust (except in the context of mergers and union antitrust)
                80020	Mergers
                80030	Bankruptcy (except in the context of priority of federal fiscal claims)
                80040	Sufficiency of evidence: typically in the context of a jury's determination of compensation for injury or death
                80050	Election of remedies: legal remedies available to injured persons or things
                80060	Liability, governmental: tort or contract actions by or against government or governmental officials other than defense of criminal actions brought under a civil rights action.
                80070	Liability, other than as in sufficiency of evidence, election of remedies, punitive damages
                80080	Liability, punitive damages
                80090	Employee Retirement Income Security Act (cf. union trust funds)
                80100	State or local government tax
                80105	State and territorial land claims
                80110	State or local government regulation, especially of business (cf. federal pre-emption of state court jurisdiction, federal pre-emption of state legislation or regulation)
                80120	Federal or state regulation of securities
                80130	Natural resources - environmental protection (cf. national supremacy: natural resources, national supremacy: pollution)
                80140	Corruption, governmental or governmental regulation of other than as in campaign spending
                80150	Zoning: constitutionality of such ordinances, or restrictions on owners' or lessors' use of real property
                80160	Arbitration (other than as pertains to labor-management or employer-employee relations (cf. union arbitration)
                80170	Federal or state consumer protection: typically under the Truth in Lending; Food, Drug and Cosmetic; and Consumer Protection Credit Acts
                80180	Patents and copyrights: patent
                80190	Patents and copyrights: copyright
                80200	Patents and copyrights: trademark
                80210	Patents and copyrights: patentability of computer processes
                80220	Federal or state regulation of transportation regulation: railroad
                80230	Federal and some few state regulations of transportation regulation: boat
                80240	Federal and some few state regulation of transportation regulation:truck, or motor carrier
                80250	Federal and some few state regulation of transportation regulation: pipeline (cf. federal public utilities regulation: gas pipeline)
                80260	Federal and some few state regulation of transportation regulation: airline
                80270	Federal and some few state regulation of public utilities regulation: electric power
                80280	Federal and some few state regulation of public utilities regulation: nuclear power
                80290	Federal and some few state regulation of public utilities regulation: oil producer
                80300	Federal and some few state regulation of public utilities regulation: gas producer
                80310	Federal and some few state regulation of public utilities regulation: gas pipeline (cf. federal transportation regulation: pipeline)
                80320	Federal and some few state regulation of public utilities regulation: radio and television (cf. cable television)
                80330	Federal and some few state regulation of public utilities regulation: cable television (cf. radio and television)
                80340	Federal and some few state regulations of public utilities regulation: telephone or telegraph company
                80350	Miscellaneous economic regulation
                90010	Comity: civil rights
                90020	Comity: criminal procedure
                90030	Comity: First Amendment
                90040	Comity: habeas corpus
                90050	Comity: military
                90060	Comity: obscenity
                90070	Comity: privacy
                90080	Comity: miscellaneous
                90090	Comity primarily removal cases, civil procedure (cf. comity, criminal and First Amendment); deference to foreign judicial tribunals
                90100	Assessment of costs or damages: as part of a court order
                90110	Federal Rules of Civil Procedure including Supreme Court Rules, application of the Federal Rules of Evidence, Federal Rules of Appellate Procedure in civil litigation, Circuit Court Rules, and state rules and admiralty rules
                90120	Judicial review of administrative agency's or administrative official's actions and procedures
                90130	Mootness (cf. standing to sue: live dispute)
                90140	Venue
                90150	No merits: writ improvidently granted
                90160	No merits: dismissed or affirmed for want of a substantial or properly presented federal question, or a nonsuit
                90170	No merits: dismissed or affirmed for want of jurisdiction (cf. judicial administration: Supreme Court jurisdiction or authority on appeal from federal district courts or courts of appeals)
                90180	No merits: adequate non-federal grounds for decision
                90190	No merits: remand to determine basis of state or federal court decision (cf. judicial administration: state law)
                90200	No merits: miscellaneous
                90210	Standing to sue: adversary parties
                90220	Standing to sue: direct injury
                90230	Standing to sue: legal injury
                90240	Standing to sue: personal injury
                90250	Standing to sue: justiciable question
                90260	Standing to sue: live dispute
                90270	Standing to sue: parens patriae standing
                90280	Standing to sue: statutory standing
                90290	Standing to sue: private or implied cause of action
                90300	Standing to sue: taxpayer's suit
                90310	Standing to sue: miscellaneous
                90320	Judicial administration: jurisdiction or authority of federal district courts or territorial courts
                90330	Judicial administration: jurisdiction or authority of federal courts of appeals
                90340	Judicial administration: Supreme Court jurisdiction or authority on appeal or writ of error, from federal district courts or courts of appeals (cf. 753)
                90350	Judicial administration: Supreme Court jurisdiction or authority on appeal or writ of error, from highest state court
                90360	Judicial administration: jurisdiction or authority of the Court of Claims
                90370	Judicial administration: Supreme Court's original jurisdiction
                90380	Judicial administration: review of non-final order
                90390	Judicial administration: change in state law (cf. no merits: remand to determine basis of state court decision)
                90400	Judicial administration: federal question (cf. no merits: dismissed for want of a substantial or properly presented federal question)
                90410	Judicial administration: ancillary or pendent jurisdiction
                90420	Judicial administration: extraordinary relief (e.g., mandamus, injunction)
                90430	Judicial administration: certification (cf. objection to reason for denial of certiorari or appeal)
                90440	Judicial administration: resolution of circuit conflict, or conflict between or among other courts
                90450	Judicial administration: objection to reason for denial of certiorari or appeal
                90460	Judicial administration: collateral estoppel or res judicata
                90470	Judicial administration: interpleader
                90480	Judicial administration: untimely filing
                90490	Judicial administration: Act of State doctrine
                90500	Judicial administration: miscellaneous
                90510	Supreme Court's certiorari, writ of error, or appeals jurisdiction
                90520	Miscellaneous judicial power, especially diversity jurisdiction
                100010	Federal-state ownership dispute (cf. Submerged Lands Act)
                100020	Federal pre-emption of state court jurisdiction
                100030	Federal pre-emption of state legislation or regulation. cf. state regulation of business. rarely involves union activity. Does not involve constitutional interpretation unless the Court says it does.
                100040	Submerged Lands Act (cf. federal-state ownership dispute)
                100050	National supremacy: commodities
                100060	National supremacy: intergovernmental tax immunity
                100070	National supremacy: marital and family relationships and property, including obligation of child support
                100080	National supremacy: natural resources (cf. natural resources - environmental protection)
                100090	National supremacy: pollution, air or water (cf. natural resources - environmental protection)
                100100	National supremacy: public utilities (cf. federal public utilities regulation)
                100110	National supremacy: state tax (cf. state tax)
                100120	National supremacy: miscellaneous
                100130	Miscellaneous federalism
                110010	Boundary dispute between states
                110020	Non-real property dispute between states
                110030	Miscellaneous interstate relations conflict
                110033	Incorporation of foreign territories
                120010	Federal taxation, typically under provisions of the Internal Revenue Code
                120020	Federal taxation of gifts, personal, business, or professional expenses
                120030	Priority of federal fiscal claims: over those of the states or private entities
                120040	Miscellaneous federal taxation (cf. national supremacy: state tax)
                130010	Legislative veto
                130015	Executive authority vis-a-vis congress or the states
                130020	Miscellaneous
                140010	Real property
                140020	Personal property
                140030	Contracts
                140040	Evidence
                140050	Civil procedure
                140060	Torts
                140070	Wills and trusts
                140080	Commercial transactions

            #### Specific Legal Provision


                100	Article I, Section 1 (delegation of powers)
                101	Article I, Section 10 (state bill of attainder, ex post facto law, or bills of credit)
                102	Article I, Section 2, Paragraph 1 (composition of the House of Representatives)
                103	Article I, Section 2, Paragraph 3 (apportionment of Representatives)
                104	Article I, Section 4, Paragraph 1 (elections clause)
                105	Article I, Section 5, Paragraph 1 (congressional qualifications)
                106	Article I, Section 6, Paragraph 1 (speech or debate clause)
                107	Article I, Section 6, Paragraph 2 (civil appointments)
                108	Article I, Section 7, Paragraph 1 (origination clause)
                109	Article I, Section 7, Paragraph 2 (separation of powers)
                110	Article I, Section 8, Paragraph 1 (taxing, spending, general welfare, or uniformity clause)
                111	Article I, Section 8, Paragraph 3 (interstate commerce clause)
                112	Article I, Section 8, Paragraph 4 (bankruptcy clause)
                113	Article I, Section 8, Paragraph 7 (postal power)
                114	Article I, Section 8, Paragraph 8 (patent and copyright clause)
                115	Article I, Section 8, Paragraph 11 (war power)
                116	Article I, Section 8, Paragraph 14 (governance of the armed forces)
                117	Article I, Section 8, Paragraph 15 (call-up of militia)
                118	Article I, Section 8, Paragraph 16 (organizing the militia)
                119	Article I, Section 8, Paragraph 17 (governance of the District of Columbia and lands purchased from the states)
                120	Article I, Section 8, Paragraph 18 (necessary and proper clause)
                121	Article I, Section 9, Paragraph 2 (suspension of the writ of habeas corpus)
                122	Article I, Section 9, Paragraph 3 (bill of attainder or ex post facto law)
                123	Article I, Section 9, Paragraph 4 (direct tax)
                124	Article I, Section 9, Paragraph 5 (export clause)
                125	Article I, Section 9, Paragraph 6 (preference to ports)
                126	Article I, Section 9, Paragraph 7 (appropriations clause)
                127	Article I, Section 10 (state bill of attainder or ex post facto law)
                128	Article I, Section 10, Paragraph 1 (contract clause)
                129	Article I, Section 10, Paragraph 2 (export-import clause)
                130	Article I, Section 10, Paragraph 3 (compact clause)
                131	Article II, Section 1 (executive power)
                132	Article II, Section 1, Paragraph 8 (oath provision)
                133	Article II, Section 2 (commander-in-chief)
                134	Article II, Section 2, Paragraph 1 (presidential pardoning power)
                135	Article II, Section 2, Paragraph 2 (appointments clause)
                136	Article III, Section 1, Paragraph 1 (judicial power)
                137	Article III, Section 1, Paragraph 2 (good behavior and compensation clause of federal judges)
                138	Article III, Section 2 (extent of judicial power)
                139	Article III, Section 2, Paragraph 1 (case or controversy requirement)
                140	Article III, Section 2, Paragraph 2 (original jurisdiction)
                141	Article III, Section 2, Paragraph 3 (vicinage requirement)
                142	Article III, Section 3 (treason clause)
                143	Article IV, Section 1 (full faith and credit clause)
                144	Article IV, Section 2, Paragraph 1 (privileges and immunities clause)
                145	Article IV, Section 2, Paragraph 2 (extradition clause)
                146	Article IV, Section 3, Paragraph 2 (property clause)
                147	Article IV, Section 4 (guarantee clause)
                148	Article VI, Section 2 (supremacy clause)
                149	Article VI, Section 3 (oath provision)
                150	Amendment Clause
                151	Article V, Section 1 (courts)
                152	'contract clause' (No Article to be added)
                153	'freedom of contract' (Again, no article)
                200	First Amendment (speech, press, and assembly)
                201	First Amendment (association)
                202	First Amendment (free exercise of religion)
                203	First Amendment (establishment of religion)
                204	First Amendment (petition clause)
                205	Fourth Amendment
                206	Fifth Amendment (double jeopardy)
                207	Fifth Amendment (due process)
                208	Fifth Amendment (grand jury)
                209	Fifth Amendment (Miranda warnings)
                210	Fifth Amendment (self-incrimination)
                211	Fifth Amendment (takings clause)
                212	Fifth Amendment (equal protection)
                213	Sixth Amendment (right to confront and cross-examine, compulsory process)
                214	Sixth Amendment (right to counsel)
                215	Sixth Amendment (right to trial by jury)
                216	Sixth Amendment (speedy trial)
                217	Sixth Amendment (other provisions)
                218	Seventh Amendment
                219	Eighth Amendment (prohibition of excessive bail)
                220	Eighth Amendment (prohibition of excessive fines)
                221	Eighth Amendment (cruel and unusual punishment)
                222	Ninth Amendment
                223	Tenth Amendment
                224	Eleventh Amendment
                225	Twelfth Amendment
                226	Thirteenth Amendment (both sections 1 and 2)
                227	Fourteenth Amendment (privileges and immunities clause)
                228	Fourteenth Amendment (reduction in representation clause)
                229	Fourteenth Amendment (citizenship clause)
                230	Fourteenth Amendment (due process)
                231	Fourteenth Amendment (equal protection)
                232	Fourteenth Amendment (enforcement clause)
                233	Fifteenth Amendment (other provisions)
                234	Fifteenth Amendment (enforcement clause)
                235	Sixteenth Amendment
                236	Seventeenth Amendment
                237	Twenty-First Amendment
                238	Twenty-Fourth Amendment
                239	Second Amendment
                240	Fourteenth Amendment (due process and equal protection)
                241	Fourteenth Amendment (takings clause)
                300	Americans with Disabilities Act
                302	Age Discrimination in Employment
                303	Aid to Families with Dependent Children provisions of the Social Security Act, plus amendments
                304	Clean Air, plus amendments
                305	Administrative Procedure, or Administrative Orders Review
                306	Atomic Energy
                307	Bankruptcy Code, Bankruptcy Act or Rules, or Bankruptcy Reform Act of 1978
                308	Medicaid provisions of the Social Security Act
                309	Medicare provisions of the Social Security Act
                310	Clayton
                311	Reconstruction Civil Rights Acts (42 U.S.C. § 1978)
                312	Reconstruction Civil Rights Acts (42 U.S.C. § 1981)
                313	Reconstruction Civil Rights Acts (42 U.S.C. § 1982)
                314	Reconstruction Civil Rights Acts (42 U.S.C. § 1983)
                315	Reconstruction Civil Rights Acts (42 U.S.C. § 1985)
                316	Reconstruction Civil Rights Acts (42 U.S.C. § 1986)
                317	Civil Rights Act of 1964 (public accommodations)
                318	Civil Rights Act of 1957
                319	Civil Rights Act of 1991
                320	Statutory provisions of the District of Columbia
                321	Equal Access to Justice
                322	Education Amendments of 1972
                323	Employee Retirement Income Security, as amended
                324	Elementary and Secondary Education
                325	Federal False Claims
                326	Communication Act of 1934, as amended
                327	Federal Employees' Compensation
                328	Civil Rights Attorney's Fees Awards
                329	Federal Employers' Liability, as amended
                330	Federal Election Campaign
                331	Family Educational Rights and Privacy (Buckley Amendment)
                332	Federal Food, Drug, and Cosmetic, and related statutes
                333	Federal Insecticide, Fungicide, and Rodenticide
                334	Fair Labor Standards
                335	Freedom of Information, Sunshine, or Privacy Act
                336	Federal Power
                337	Federal Trade Commission
                338	Federal Water Pollution Control (Clean Water), plus amendments
                339	Omnibus Crime Control and Safe Streets, National Firearms, Organized Crime Control, Comprehensive Crime Control, or Gun Control Acts
                340	Education of the Handicapped, Education for All Handicapped Children, or Individuals with Disabilities Education Acts, or related statutes, as amended
                341	28 U.S.C. § 2241-2255 (habeas corpus)
                342	Fair Housing
                343	Interstate Commerce, as amended
                344	Immigration and Naturalization, Immigration, Nationality, or Illegal Immigration Reform and Immigrant Responsibility Acts, as amended
                345	Internal Revenue Code and pre-IRC revenue acts
                346	Internal Security (also see 369)
                347	Jencks
                348	Jones, or Death on the High Seas
                349	Longshoremen and Harbor Workers' Compensation
                350	Labor-Management Relations
                351	Labor-Management Reporting and Disclosure
                352	Motor Carrier
                353	Miller
                354	National Environmental Policy
                355	Natural Gas, or Natural Gas Policy Acts
                356	National Labor Relations, as amended
                357	Norris-LaGuardia
                358	Occupational Safety and Health
                359	Public Utility Regulatory Policy
                360	Rehabilitation
                361	Religious Freedom Restoration
                362	Racketeer Influenced and Corrupt Organizations
                363	Railway Labor
                364	Robinson-Patman
                365	Securities Act of 1933, the Securities and Exchange Act of 1934, or the Williams Act
                366	Selective Service, Military Selective Service, or Universal Military Service and Training Acts
                367	Sherman
                368	Submerged Lands Acts
                369	Smith, Subversive Activities Control, Communist Control, or other similar federal legislation (also see 346)
                370	Social Security, as amended, including Social Security Disability Benefits Reform Act
                371	Supplemental Security Income
                372	State Law
                373	Truth in Lending
                374	Federal Tort Claims, or Alien Tort Statute
                375	Tucker
                376	Trading with the Enemy Act, as amended
                377	Universal Code of Military Justice
                378	Voting Rights Act of 1965, plus amendments
                379	Reconstruction Civil Rights Acts (42 U.S.C. § 1971)
                380	Reconstruction Civil Rights Acts (42 U.S.C. § 1999)
                381	Civil Rights Act of 1964 (Title II)
                382	Civil Rights Act of 1964 (Title IV)
                383	Civil Rights Act of 1964 (other)
                384	Civil Rights Act of 1964 (Title VII)
                385	Civil Rights Act of 1964 (Title IX)
                387	Civil Rights Act of 1964 (Title VI)
                388	Federal Arbitration Act
                389	Judiciary Act of 1789
                400	Federal Rules of Civil Procedure, including Appellate Procedure, or relevant rules of a circuit court Judicial Code, and admiralty rules
                401	Federal Rules of Criminal Procedure, or relevant rules of a circuit court
                402	Federal Rules of Evidence
                403	Supreme Court Rules
                500	Abstention Doctrine
                501	Retroactive application of a constitutional right
                502	Exclusionary Rule (Fourth Amendment)
                503	Exclusionary Rule (Right to Counsel)
                504	Exclusionary Rule (Miranda warnings)
                505	Harmless Error
                506	Res Judicata
                507	Estoppel
                508	Writ Improvidently Granted
                509	Treaty
                510	Interstate Compact
                511	Executive Order
                512	Territory Statute
                513	International Law
                514	Emergency Price Control
                600	Infrequently litigated statutes
                800	State or Local Law Regulation
                900	No Legal Provision
            """
        ),

    ],
)

layout = dbc.Row([column1])