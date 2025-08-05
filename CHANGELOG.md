# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## [1.16.0](https://github.com/box/box-python-sdk-gen/compare/v1.15.0...v1.16.0) (2025-08-05)


### Bug Fixes

* Specify events `next_stream_position` property type as `int` (box/box-openapi[#535](https://github.com/box/box-python-sdk-gen/issues/535)) ([#644](https://github.com/box/box-python-sdk-gen/issues/644)) ([64069db](https://github.com/box/box-python-sdk-gen/commit/64069db8da33988c173380defd6be065daa02496))


### New Features and Enhancements

* Add AI spreadsheet processor (box/box-openapi[#533](https://github.com/box/box-python-sdk-gen/issues/533)) ([#630](https://github.com/box/box-python-sdk-gen/issues/630)) ([6635757](https://github.com/box/box-python-sdk-gen/commit/66357578218913240bc923cb0dc771157ec95f54))
* Add Archive Public API (box/box-openapi[#540](https://github.com/box/box-python-sdk-gen/issues/540)) ([#651](https://github.com/box/box-python-sdk-gen/issues/651)) ([c36d1db](https://github.com/box/box-python-sdk-gen/commit/c36d1dbff42c89876c037983c792c5c7282459cc))
* Add new Hubs APIs and Hubs items API (box/box-openapi[#538](https://github.com/box/box-python-sdk-gen/issues/538)) ([#645](https://github.com/box/box-python-sdk-gen/issues/645)) ([1daa3e8](https://github.com/box/box-python-sdk-gen/commit/1daa3e8814403c78ed2a1d64187b8e4c379028fe))
* Add new property for network exception retry strategy (box/box-codegen[#763](https://github.com/box/box-python-sdk-gen/issues/763)) ([#650](https://github.com/box/box-python-sdk-gen/issues/650)) ([13f9593](https://github.com/box/box-python-sdk-gen/commit/13f9593dbc4a45d094ee5709d602188ef341a1a5))
* Add new schema for `Metadata Error` (box/box-openapi[#539](https://github.com/box/box-python-sdk-gen/issues/539)) ([#646](https://github.com/box/box-python-sdk-gen/issues/646)) ([49d7f34](https://github.com/box/box-python-sdk-gen/commit/49d7f349e1be4e23939ef10db1edfc6042b98175))
* Allow injecting private key decrypt mechanism for JWT (box/box-codegen[#754](https://github.com/box/box-python-sdk-gen/issues/754)) ([#636](https://github.com/box/box-python-sdk-gen/issues/636)) ([4ea0af5](https://github.com/box/box-python-sdk-gen/commit/4ea0af5f8f5b5516a7c23d7912c34690c017db29))
* Improve webhook validation checks (box/box-codegen[#745](https://github.com/box/box-python-sdk-gen/issues/745)) ([#628](https://github.com/box/box-python-sdk-gen/issues/628)) ([f0ece63](https://github.com/box/box-python-sdk-gen/commit/f0ece639d761c765b3bc59fbe3ba8582af755178))
* Support Hubs beta endpoints (box/box-openapi[#531](https://github.com/box/box-python-sdk-gen/issues/531)) ([#622](https://github.com/box/box-python-sdk-gen/issues/622)) ([b5e95fe](https://github.com/box/box-python-sdk-gen/commit/b5e95fe5b219d067028aa395170718eca0d62189))
* Support new tools in AI Studio (box/box-openapi[#534](https://github.com/box/box-python-sdk-gen/issues/534))  ([#633](https://github.com/box/box-python-sdk-gen/issues/633)) ([ac76eb2](https://github.com/box/box-python-sdk-gen/commit/ac76eb2d7c5560b30c4cec171dd90b0a0ece4ab5))

## [1.15.0](https://github.com/box/box-python-sdk-gen/compare/v1.14.0...v1.15.0) (2025-06-12)


### Bug Fixes

* Compute webhook signature with and without escaping the body (box/box-codegen[#737](https://github.com/box/box-python-sdk-gen/issues/737)) ([#607](https://github.com/box/box-python-sdk-gen/issues/607)) ([e5118b8](https://github.com/box/box-python-sdk-gen/commit/e5118b8a257a042510374d91bd62a1f98c662fef))
* Fix downscope token to use `retrieveToken` method for token retrieval (box/box-codegen[#731](https://github.com/box/box-python-sdk-gen/issues/731)) ([#598](https://github.com/box/box-python-sdk-gen/issues/598)) ([e492685](https://github.com/box/box-python-sdk-gen/commit/e4926851edccd4ee7e66157050cedd0d01cec5ea))
* Fix slash escaping when calculating webhook signature (box/box-codegen[#736](https://github.com/box/box-python-sdk-gen/issues/736)) ([#603](https://github.com/box/box-python-sdk-gen/issues/603)) ([430b175](https://github.com/box/box-python-sdk-gen/commit/430b1754ec840582e28a277c6c8d369cbe7ebdf5))
* Use constant-time comparison for HMAC signatures (box/box-codegen[#739](https://github.com/box/box-python-sdk-gen/issues/739)) ([#610](https://github.com/box/box-python-sdk-gen/issues/610)) ([6f6660c](https://github.com/box/box-python-sdk-gen/commit/6f6660c8f3aa2b7b75b0fcd4ed015d8d761cd77f))


### New Features and Enhancements

* Add AI agents warnings; allow for more types of metadata value (box/box-openapi[#520](https://github.com/box/box-python-sdk-gen/issues/520)) ([#567](https://github.com/box/box-python-sdk-gen/issues/567)) ([86aa1cc](https://github.com/box/box-python-sdk-gen/commit/86aa1ccadac9acead7bceeafb50e45f38eb2d9cc))
* Add Shield Lists APIs (box/box-openapi[#528](https://github.com/box/box-python-sdk-gen/issues/528)) ([#601](https://github.com/box/box-python-sdk-gen/issues/601)) ([f980f65](https://github.com/box/box-python-sdk-gen/commit/f980f6544a58a5c64ab0b3ec13b2771b81ea25ed))
* Add support of IBM models to AI API (box/box-openapi[#522](https://github.com/box/box-python-sdk-gen/issues/522)) ([#568](https://github.com/box/box-python-sdk-gen/issues/568)) ([767547a](https://github.com/box/box-python-sdk-gen/commit/767547ae070909852800c447e65cbcc95b97c5a3))
* Update legal holds and AI models (box/box-openapi[#526](https://github.com/box/box-python-sdk-gen/issues/526)) ([#599](https://github.com/box/box-python-sdk-gen/issues/599)) ([d56228d](https://github.com/box/box-python-sdk-gen/commit/d56228d81bd9777af5431ccc9d05233e13a0c2ed))

## [1.14.0](https://github.com/box/box-python-sdk-gen/compare/v1.13.0...v1.14.0) (2025-05-02)


### Bug Fixes

* set default timeouts for requests (box/box-codegen[#707](https://github.com/box/box-python-sdk-gen/issues/707)) ([#552](https://github.com/box/box-python-sdk-gen/issues/552)) ([66b87c8](https://github.com/box/box-python-sdk-gen/commit/66b87c8986ce2f5fdb3a9eac995ef8a9643bcd76))


### New Features and Enhancements

* Add security settings properties on sign template schema (box/box-openapi[#518](https://github.com/box/box-python-sdk-gen/issues/518)) ([#543](https://github.com/box/box-python-sdk-gen/issues/543)) ([0a45d21](https://github.com/box/box-python-sdk-gen/commit/0a45d218d1aa3fa62da7b5c8c01506fb657c0b36))
* Support sensitive data sanitization in errors (box/box-codegen[#695](https://github.com/box/box-python-sdk-gen/issues/695)) ([#533](https://github.com/box/box-python-sdk-gen/issues/533)) ([abb7b1d](https://github.com/box/box-python-sdk-gen/commit/abb7b1d16a192edd99ff1fc4fb7c4caf79ee5f10))

## [1.13.0](https://github.com/box/box-python-sdk-gen/compare/v1.12.0...v1.13.0) (2025-03-18)


### Bug Fixes

* Add `verification_phone_number` property to create sign request (box/box-openapi[#515](https://github.com/box/box-python-sdk-gen/issues/515)) ([#503](https://github.com/box/box-python-sdk-gen/issues/503)) ([6d19d19](https://github.com/box/box-python-sdk-gen/commit/6d19d197481a578d7d5ad8d632ac6f5c06bd3dce))


### New Features and Enhancements

* Add find app item for shared link endpoint (box/box-openapi[#514](https://github.com/box/box-python-sdk-gen/issues/514)) ([#502](https://github.com/box/box-python-sdk-gen/issues/502)) ([fd6c693](https://github.com/box/box-python-sdk-gen/commit/fd6c6933f0fb518830e9ac810fd511a0cf60b429))
* Add Integration Mappings Teams API (box/box-openapi[#517](https://github.com/box/box-python-sdk-gen/issues/517)) ([#505](https://github.com/box/box-python-sdk-gen/issues/505)) ([d1aa250](https://github.com/box/box-python-sdk-gen/commit/d1aa250fb01fbf742daf266d4458ba2eab2c5669))
* Support upload with preflight check (box/box-codegen[#676](https://github.com/box/box-python-sdk-gen/issues/676)) ([#515](https://github.com/box/box-python-sdk-gen/issues/515)) ([bb4597e](https://github.com/box/box-python-sdk-gen/commit/bb4597e40d49e20eca44c4414e406b1352af1a2b))

## [1.12.0](https://github.com/box/box-python-sdk-gen/compare/v1.11.1...v1.12.0) (2025-02-20)


### Bug Fixes

* Fix handling responses with invalid JSON (box/box-codegen[#667](https://github.com/box/box-python-sdk-gen/issues/667)) ([#485](https://github.com/box/box-python-sdk-gen/issues/485)) ([46399d8](https://github.com/box/box-python-sdk-gen/commit/46399d8d91d9a22c75e03e870b091cac6d81237f)), closes [#470](https://github.com/box/box-python-sdk-gen/issues/470)


### New Features and Enhancements

* Support AI Studio API (box/box-codegen[#626](https://github.com/box/box-python-sdk-gen/issues/626)) ([#483](https://github.com/box/box-python-sdk-gen/issues/483)) ([bd7fefa](https://github.com/box/box-python-sdk-gen/commit/bd7fefad8f2d941676732ea66c5b0d75bae9e703))

### [1.11.1](https://github.com/box/box-python-sdk-gen/compare/v1.11.0...v1.11.1) (2025-02-12)


### Bug Fixes

* Fix proxy usage (box/box-codegen[#662](https://github.com/box/box-python-sdk-gen/issues/662)) ([#476](https://github.com/box/box-python-sdk-gen/issues/476)) ([e1d62ac](https://github.com/box/box-python-sdk-gen/commit/e1d62ac5a8063bf37244329329100752c3a069af))

## [1.11.0](https://github.com/box/box-python-sdk-gen/compare/v1.10.0...v1.11.0) (2025-02-06)


### Bug Fixes

* Correct types of `paged` and `thumb` properties in File representation (box/box-openapi[#503](https://github.com/box/box-python-sdk-gen/issues/503)) ([#451](https://github.com/box/box-python-sdk-gen/issues/451)) ([e818fa6](https://github.com/box/box-python-sdk-gen/commit/e818fa6c9c80e61a293fc24ed6f1a15978681662))


### New Features and Enhancements

* Add Box Sign shared requests (box/box-openapi[#504](https://github.com/box/box-python-sdk-gen/issues/504)) ([#453](https://github.com/box/box-python-sdk-gen/issues/453)) ([3590918](https://github.com/box/box-python-sdk-gen/commit/359091873d26111b82f000e7837553cc799f2433))
* feat: Add hubs support to `/ai/ask`. Replace type of `items` parameter from `List[AiItemBase]` to `List[AiItemAsk]` in `create_ai_ask` method (box/box-openapi[#506](https://github.com/box/box-python-sdk-gen/issues/506)) ([#466](https://github.com/box/box-python-sdk-gen/issues/466)) ([29f0364](https://github.com/box/box-python-sdk-gen/commit/29f03649f3ec1471e859609d2b8bd77ad5d09106))
* Update `/ai/extract_structured` response schema (box/box-codegen[#641](https://github.com/box/box-python-sdk-gen/issues/641)) ([#459](https://github.com/box/box-python-sdk-gen/issues/459)) ([7c73cea](https://github.com/box/box-python-sdk-gen/commit/7c73ceaa8888332b23bca4d6b64ef4999f942940))

## [1.10.0](https://github.com/box/box-python-sdk-gen/compare/v1.9.0...v1.10.0) (2025-01-21)


### Bug Fixes

* Add missing token scope (box/box-openapi[#490](https://github.com/box/box-python-sdk-gen/issues/490)) ([#420](https://github.com/box/box-python-sdk-gen/issues/420)) ([41afe8b](https://github.com/box/box-python-sdk-gen/commit/41afe8bcbfc20e3ff22d34a273dcb416afb455da))
* Fix invalid variant config for Integration mapping Slack (box/box-openapi[#492](https://github.com/box/box-python-sdk-gen/issues/492)) ([#423](https://github.com/box/box-python-sdk-gen/issues/423)) ([d03ccd4](https://github.com/box/box-python-sdk-gen/commit/d03ccd46b88c71450c1c67ecef439e25b97cbad7))
* order of fields in the `IntegrationMapping` schema (box/box-openapi[#497](https://github.com/box/box-python-sdk-gen/issues/497)) ([#438](https://github.com/box/box-python-sdk-gen/issues/438)) ([13dea88](https://github.com/box/box-python-sdk-gen/commit/13dea88c4e43748eed600f55a638c14ef0a1a60a))


### New Features and Enhancements

* Support Box Doc Gen API (box/box-codegen[#644](https://github.com/box/box-python-sdk-gen/issues/644)) ([#446](https://github.com/box/box-python-sdk-gen/issues/446)) ([41fa63c](https://github.com/box/box-python-sdk-gen/commit/41fa63c0a3c957a34b03163dfeaa44a03a5873ff))

## [1.9.0](https://github.com/box/box-python-sdk-gen/compare/v1.8.0...v1.9.0) (2024-12-30)


### Bug Fixes

* Remove unused parameter from `SignRequest` (box/box-openapi[#489](https://github.com/box/box-python-sdk-gen/issues/489)) ([#411](https://github.com/box/box-python-sdk-gen/issues/411)) ([578d9b4](https://github.com/box/box-python-sdk-gen/commit/578d9b48da7e55d2e3e4736c871400dc90d826b1))


### New Features and Enhancements

* Add `ai_agent` info to `AiResponse` (box/box-openapi[#485](https://github.com/box/box-python-sdk-gen/issues/485)) ([#402](https://github.com/box/box-python-sdk-gen/issues/402)) ([351a5b8](https://github.com/box/box-python-sdk-gen/commit/351a5b8dfbc8a0095bafbbf0245d8575217fc3c9))
* Add support for replacing the network client implementation (box/box-codegen[#629](https://github.com/box/box-python-sdk-gen/issues/629)) ([#415](https://github.com/box/box-python-sdk-gen/issues/415)) ([fb118dd](https://github.com/box/box-python-sdk-gen/commit/fb118ddb1cbfb1d6a72e657bed57088fdff1ec02))
* Allow for customizing retry strategy (box/box-codegen[#635](https://github.com/box/box-python-sdk-gen/issues/635)) ([#418](https://github.com/box/box-python-sdk-gen/issues/418)) ([8dfb3ed](https://github.com/box/box-python-sdk-gen/commit/8dfb3ed13196de37a78a53325079e284c7e921d5))
* Support optional `userId` parameter for updating files, folders and web links (box/box-openapi[#488](https://github.com/box/box-python-sdk-gen/issues/488)) ([#406](https://github.com/box/box-python-sdk-gen/issues/406)) ([d9cff4c](https://github.com/box/box-python-sdk-gen/commit/d9cff4c6adc9c5cc9ce1edf73dffe8ac5979ce71))
* Support webhook message validation (box/box-codegen[#631](https://github.com/box/box-python-sdk-gen/issues/631)) ([#416](https://github.com/box/box-python-sdk-gen/issues/416)) ([0fec20b](https://github.com/box/box-python-sdk-gen/commit/0fec20b281fe195f0dd6aaf8f164bdd414587fc4))

## [1.8.0](https://github.com/box/box-python-sdk-gen/compare/v1.7.0...v1.8.0) (2024-12-02)


### Bug Fixes

* Fix enums usage (box/box-codegen[#615](https://github.com/box/box-python-sdk-gen/issues/615)) ([#387](https://github.com/box/box-python-sdk-gen/issues/387)) ([a9abccb](https://github.com/box/box-python-sdk-gen/commit/a9abccb8e552c971774ea1a9fa2096395a40317b)), closes [#385](https://github.com/box/box-python-sdk-gen/issues/385)
* Support status codes with no content (box/box-codegen[#604](https://github.com/box/box-python-sdk-gen/issues/604)) ([#378](https://github.com/box/box-python-sdk-gen/issues/378)) ([051716c](https://github.com/box/box-python-sdk-gen/commit/051716c84b4f0ab32b82608f94e3cf3ba09b390b))
* update collaboration, metadata and collection resources (box/box-openapi[#483](https://github.com/box/box-python-sdk-gen/issues/483)) ([#380](https://github.com/box/box-python-sdk-gen/issues/380)) ([0d45fed](https://github.com/box/box-python-sdk-gen/commit/0d45fedc0b7b96234ef3901f412f259b1cae4c1a))


### New Features and Enhancements

* Expose method for making custom HTTP requests (box/box-codegen[#610](https://github.com/box/box-python-sdk-gen/issues/610)) ([#393](https://github.com/box/box-python-sdk-gen/issues/393)) ([55a23d9](https://github.com/box/box-python-sdk-gen/commit/55a23d9d6840642c248ab3b967ad5c2635484c8c))
* Support getting file download URL and file thumbnail URL (box/box-codegen[#617](https://github.com/box/box-python-sdk-gen/issues/617)) ([#397](https://github.com/box/box-python-sdk-gen/issues/397)) ([fd609ab](https://github.com/box/box-python-sdk-gen/commit/fd609ab9fe94da43b1a71815597c49471e157bb8))

## [1.7.0](https://github.com/box/box-codegen/compare/v1.6.0...v1.7.0) (2024-11-04)


### New Features and Enhancements

* Support get collection by ID endpoint (box/box-codegen[#595](https://github.com/box/box-codegen/issues/595)) ([#366](https://github.com/box/box-codegen/issues/366)) ([1db5722](https://github.com/box/box-codegen/commit/1db5722f7d02694739f1a52a6b2ebe0c406960b0)), closes [#355](https://github.com/box/box-codegen/issues/355)

## [1.6.0](https://github.com/box/box-codegen/compare/v1.5.1...v1.6.0) (2024-10-30)


### Bug Fixes

* Set stream position to 0 for multipart requests (box/box-codegen[#581](https://github.com/box/box-codegen/issues/581)) ([#348](https://github.com/box/box-codegen/issues/348)) ([fa6942c](https://github.com/box/box-codegen/commit/fa6942c231024947250955ccc52f352744ab5f38))
* Update client error schema (box/box-openapi[#467](https://github.com/box/box-codegen/issues/467)) ([#347](https://github.com/box/box-codegen/issues/347)) ([a42a253](https://github.com/box/box-codegen/commit/a42a2532337c79d20b6524fda0acf717d9ccbd5f))
* Use original stream position when retrying requests (box/box-codegen[#583](https://github.com/box/box-codegen/issues/583)) ([#358](https://github.com/box/box-codegen/issues/358)) ([060b4dc](https://github.com/box/box-codegen/commit/060b4dc2b8bbbc1e17cce0fc049394e0527952b7))
* use raw `docstrings` when comments contain backslash (box/box-codegen[#571](https://github.com/box/box-codegen/issues/571)) ([#330](https://github.com/box/box-codegen/issues/330)) ([8dd8cb7](https://github.com/box/box-codegen/commit/8dd8cb71105c200bd03f5f894a4dbfb42baf0865))


### New Features and Enhancements

* Add `download_file_to_output_stream` method to `DownloadsManager` (box/box-codegen[#575](https://github.com/box/box-codegen/issues/575)) ([#334](https://github.com/box/box-codegen/issues/334)) ([6820d08](https://github.com/box/box-codegen/commit/6820d08f37c5c0605a580391bef2dc4f2a384c00))
* add AI LLM endpoint AWS `params` (box/box-openapi[#478](https://github.com/box/box-codegen/issues/478)) ([#354](https://github.com/box/box-codegen/issues/354)) ([c8fa2c1](https://github.com/box/box-codegen/commit/c8fa2c1131154d07a500290db6a7b34b06005c2b))

### [1.5.1](https://github.com/box/box-codegen/compare/v1.5.0...v1.5.1) (2024-09-19)


### Bug Fixes

* Fix proxy `url` without proxy credentials (box/box-codegen[#568](https://github.com/box/box-codegen/issues/568)) ([#322](https://github.com/box/box-codegen/issues/322)) ([fb19160](https://github.com/box/box-codegen/commit/fb19160307b58d5f08bb12e0f846d71ff936ad6a)), closes [#318](https://github.com/box/box-codegen/issues/318)
* Stop sending last empty chunk for chunk upload (box/box-codegen[#569](https://github.com/box/box-codegen/issues/569)) ([#324](https://github.com/box/box-codegen/issues/324)) ([1605f04](https://github.com/box/box-codegen/commit/1605f0495994b333e735bc98f28fa714324b75f5)), closes [#321](https://github.com/box/box-codegen/issues/321)

## [1.5.0](https://github.com/box/box-codegen/compare/v1.4.1...v1.5.0) (2024-09-18)


### Bug Fixes

* Add the missing license to `setup.py` (box/box-codegen[#562](https://github.com/box/box-codegen/issues/562)) ([#307](https://github.com/box/box-codegen/issues/307)) ([679d789](https://github.com/box/box-codegen/commit/679d7891b2a20e7407b8c9f00bd95c3b294ab861))
* Fix variants in metadata query results (box/box-openapi[#456](https://github.com/box/box-codegen/issues/456)) ([#313](https://github.com/box/box-codegen/issues/313)) ([8830303](https://github.com/box/box-codegen/commit/883030335e2a3c12a5e0b01d8a82df30ccce16a6))


### New Features and Enhancements

* Add support for proxy (box/box-codegen[#559](https://github.com/box/box-codegen/issues/559)) ([#302](https://github.com/box/box-codegen/issues/302)) ([3d881ac](https://github.com/box/box-codegen/commit/3d881acdebf2b18e2f0f82211f5abdcc32d1ddb0))
* Introduce `raw_data` field for storing raw `json` response (box/box-codegen[#566](https://github.com/box/box-codegen/issues/566)) ([#319](https://github.com/box/box-codegen/issues/319)) ([3776dc3](https://github.com/box/box-codegen/commit/3776dc3d44bc09eb68da99f45e36e058dca2607e))
* Support `ai/extract` and `ai/extract_structured` endpoints (box/box-codegen[#564](https://github.com/box/box-codegen/issues/564)) ([#317](https://github.com/box/box-codegen/issues/317)) ([b3d8da4](https://github.com/box/box-codegen/commit/b3d8da41007a9d47b73b699fd84da6f9540866d2))
* Support App item associations (box/box-codegen[#561](https://github.com/box/box-codegen/issues/561)) ([#299](https://github.com/box/box-codegen/issues/299)) ([8b6ea0b](https://github.com/box/box-codegen/commit/8b6ea0bbec719a36eb11b6d214c08801c4f1a40b))

### [1.4.1](https://github.com/box/box-codegen/compare/v1.4.0...v1.4.1) (2024-08-30)


### Bug Fixes

* Do not store data in-memory during download process in Python (box/box-codegen[#557](https://github.com/box/box-codegen/issues/557)) ([#294](https://github.com/box/box-codegen/issues/294)) ([7c645ae](https://github.com/box/box-codegen/commit/7c645aea9fa8575531e0b40ffc997a0f65b6e409))

## [1.4.0](https://github.com/box/box-codegen/compare/v1.3.0...v1.4.0) (2024-08-23)


### Bug Fixes

* Add missing fields to Sign Template Signer and fix AI schema (box/box-openapi[#451](https://github.com/box/box-codegen/issues/451)) ([#281](https://github.com/box/box-codegen/issues/281)) ([0708351](https://github.com/box/box-codegen/commit/0708351171eca1fe4914b823a4257bbabd3cd075))
* Fix `IntegrationMapping` schemas (box/box-codegen[#551](https://github.com/box/box-codegen/issues/551)) ([#279](https://github.com/box/box-codegen/issues/279)) ([0337e06](https://github.com/box/box-codegen/commit/0337e06c6bf6d35dd51409c429b7fef295f5a406))


### New Features and Enhancements

* Add new parameters to Box AI methods and introduce `AiResponseFull` variant (box/box-openapi[#446](https://github.com/box/box-codegen/issues/446)) ([#277](https://github.com/box/box-codegen/issues/277)) ([1267a21](https://github.com/box/box-codegen/commit/1267a215fbc8292059603665a53b0159d7a1242c))
* Include URL into `FetchOptions` (box/box-codegen[#549](https://github.com/box/box-codegen/issues/549)) ([#283](https://github.com/box/box-codegen/issues/283)) ([dd05b1c](https://github.com/box/box-codegen/commit/dd05b1c2b1687d8647f4116c022dbf1890984adc))

## [1.3.0](https://github.com/box/box-codegen/compare/v1.2.0...v1.3.0) (2024-08-12)


### Bug Fixes

* Fix fetch method for multipart request (box/box-codegen[#545](https://github.com/box/box-codegen/issues/545)) ([#266](https://github.com/box/box-codegen/issues/266)) ([08a0818](https://github.com/box/box-codegen/commit/08a0818995d64995c3e2720a459f9221c9ca1dea))


### New Features and Enhancements

* Parametrise chunked uploads endpoint urls (box/box-openapi[#444](https://github.com/box/box-codegen/issues/444)) ([#264](https://github.com/box/box-codegen/issues/264)) ([b5bce24](https://github.com/box/box-codegen/commit/b5bce24478c70ae6bb997adc773a0e2a76223568))

## [1.2.0](https://github.com/box/box-codegen/compare/v1.1.0...v1.2.0) (2024-07-25)


### Bug Fixes

* Improve chunked upload reliability ([#224](https://github.com/box/box-codegen/issues/224)) ([05f0353](https://github.com/box/box-codegen/commit/05f035354a76dac0d71849523e4a28641ac92aee))


### New Features and Enhancements

* Add `is_active` parameter to user collaboration (box/box-openapi[#437](https://github.com/box/box-codegen/issues/437)) ([#222](https://github.com/box/box-codegen/issues/222)) ([2b7bbe4](https://github.com/box/box-codegen/commit/2b7bbe41ed23e50c6717148fa5e9e2c24a3f5897))
* Retry request with status code `202` `(box/box-codegen[#511](https://github.com/box/box-codegen/issues/511))` ([#204](https://github.com/box/box-codegen/issues/204)) ([f50ad6e](https://github.com/box/box-codegen/commit/f50ad6e236003901792eb333738020cbdd8c8ae3))
* Support AI Agent API (box/box-codegen[#531](https://github.com/box/box-codegen/issues/531)) ([#229](https://github.com/box/box-codegen/issues/229)) ([c565383](https://github.com/box/box-codegen/commit/c5653839e1a150377e7d5c4764d4c2a7b7d07c4a))
* Support sending fields with `null` value (box/box-codegen[#528](https://github.com/box/box-codegen/issues/528)) ([#230](https://github.com/box/box-codegen/issues/230)) ([f91076e](https://github.com/box/box-codegen/commit/f91076e1bfbccae4a0dff4b66d7bafb5357858c5)), closes [#202](https://github.com/box/box-codegen/issues/202)

## [1.1.0](https://github.com/box/box-codegen/compare/v1.0.0...v1.1.0) (2024-06-12)


### Bug Fixes

* Fix CI for auto update pull requests (box/box-codegen[#506](https://github.com/box/box-codegen/issues/506)) ([#187](https://github.com/box/box-codegen/issues/187)) ([5e59f69](https://github.com/box/box-codegen/commit/5e59f69591e01cd2caf0033e0023061093989aa5))


### New Features and Enhancements

* add missing marker pagination fields and introduce new event type `AppItemEventSource` `(box/box-openapi[#431](https://github.com/box/box-codegen/issues/431))` ([#189](https://github.com/box/box-codegen/issues/189)) ([8d22ce2](https://github.com/box/box-codegen/commit/8d22ce20d57f4b5dcb5b344ff6bfc67bcaa3568d))

## [1.0.0](https://github.com/box/box-codegen/compare/v0.6.5...v1.0.0) (2024-05-20)


### Bug Fixes

* Change base urls (box/box-codegen[#491](https://github.com/box/box-codegen/issues/491)) ([#167](https://github.com/box/box-codegen/issues/167)) ([7f7cb20](https://github.com/box/box-codegen/commit/7f7cb201720bf04efd25c21c1fb131b9f38e5f77))
* Fix schemas for updating classification on a file and folder (box/box-openapi[#423](https://github.com/box/box-codegen/issues/423)) ([#156](https://github.com/box/box-codegen/issues/156)) ([1c4bee1](https://github.com/box/box-codegen/commit/1c4bee1874dcf7f164cbe85ae200883bd4e81ea2))
* Make `PartAccumulator` class internal ([#169](https://github.com/box/box-codegen/issues/169)) ([16726e7](https://github.com/box/box-codegen/commit/16726e7324820572da50c3079b2fe449b103173d))


### New Features and Enhancements

* Add `suppressNotifications` and `externalSystemName` fields for Box Sign (box/box-openapi[#425](https://github.com/box/box-codegen/issues/425)) ([#165](https://github.com/box/box-codegen/issues/165)) ([34ea7c2](https://github.com/box/box-codegen/commit/34ea7c2275017a2d3256361de277272f36859974))
* Move schemas to separate modules (box/box-codegen[#483](https://github.com/box/box-codegen/issues/483)) ([#149](https://github.com/box/box-codegen/issues/149)) ([0ba0142](https://github.com/box/box-codegen/commit/0ba01427e8cffb3fa72892afbf281b11dac4f1ed))
* support excluding endpoints and schemas in parser (box/box-codegen[#487](https://github.com/box/box-codegen/issues/487)) ([#150](https://github.com/box/box-codegen/issues/150)) ([13308c4](https://github.com/box/box-codegen/commit/13308c48700528bd870ca97035d0c3f04e66c299))

### [0.6.5](https://github.com/box/box-codegen/compare/v0.6.4...v0.6.5) (2024-05-09)


### Bug Fixes

* Add documentation to folder resource (box/box-openapi[#421](https://github.com/box/box-codegen/issues/421)) ([#144](https://github.com/box/box-codegen/issues/144)) ([ca4e62e](https://github.com/box/box-codegen/commit/ca4e62eafe6b508f92bfda4c7d7075e69c36fc31))
* Ensure `AuthorizationManager` in authentication classes is initialized with `NetworkSession` object (box/box-codegen[#469](https://github.com/box/box-codegen/issues/469)) ([#113](https://github.com/box/box-codegen/issues/113)) ([a5577c7](https://github.com/box/box-codegen/commit/a5577c734b5ca18567b423075661964735f6e46a))
* Fix Box AI endpoints (box/box-openapi[#418](https://github.com/box/box-codegen/issues/418)) ([#139](https://github.com/box/box-codegen/issues/139)) ([de2b8a3](https://github.com/box/box-codegen/commit/de2b8a3874d8647d9fc77d61ff998bf7d5400a69))
* Fix deserialization logic (box/box-codegen[#476](https://github.com/box/box-codegen/issues/476)) ([#126](https://github.com/box/box-codegen/issues/126)) ([90ea928](https://github.com/box/box-codegen/commit/90ea928aec6bf6a2d22c7156a570d2ade57daf80))


### New Features and Enhancements

* Support Box AI endpoints (box/box-openapi[#416](https://github.com/box/box-codegen/issues/416)) ([#137](https://github.com/box/box-codegen/issues/137)) ([7a90c0c](https://github.com/box/box-codegen/commit/7a90c0c10b29af35307fd1fbb3931442c4aad06b))
* Support revoking and downscoping token for `BoxDeveloperTokenAuth` (box/box-codegen[#472](https://github.com/box/box-codegen/issues/472)) ([#115](https://github.com/box/box-codegen/issues/115)) ([1b9628c](https://github.com/box/box-codegen/commit/1b9628c321b1ade72cbadac7ef4e63e4e7b132e0))
* Support union of primitives and objects (box/box-codegen[#481](https://github.com/box/box-codegen/issues/481)) ([#140](https://github.com/box/box-codegen/issues/140)) ([d08c3e9](https://github.com/box/box-codegen/commit/d08c3e9987c3d655b2741e412cfafa48d1959b6e))

### [0.6.4](https://github.com/box/box-codegen/compare/v0.6.3...v0.6.4) (2024-04-04)


### Bug Fixes

* **docs:** fixes for chunked uploads docs (box/box-codegen[#457](https://github.com/box/box-codegen/issues/457)) ([#106](https://github.com/box/box-codegen/issues/106)) ([65f40f5](https://github.com/box/box-codegen/commit/65f40f55a5bd020fd9e1e2db31d4979a4f10d4cf))


### New Features and Enhancements

* Assign default value to fields and args of type enum with only one value (box/box-codegen[#465](https://github.com/box/box-codegen/issues/465)) ([#108](https://github.com/box/box-codegen/issues/108)) ([f884b60](https://github.com/box/box-codegen/commit/f884b600b8be77e8fdbbff553c066a927090c42d))
* Change `asUser` and `asEnterprise` method names (box/box-codegen[#464](https://github.com/box/box-codegen/issues/464)) ([#103](https://github.com/box/box-codegen/issues/103)) ([bb03852](https://github.com/box/box-codegen/commit/bb03852443fa0c3fcd8fec60cb10e5bff607abe5))

### [0.6.3](https://github.com/box/box-codegen/compare/v0.6.2...v0.6.3) (2024-03-26)


### New Features and Enhancements

* Support datetime (box/box-codegen[#459](https://github.com/box/box-codegen/issues/459)) ([#98](https://github.com/box/box-codegen/issues/98)) ([5a4d1eb](https://github.com/box/box-codegen/commit/5a4d1ebec872faefeecb82fbc0262ba52cb7af9a))

### [0.6.2](https://github.com/box/box-codegen/compare/v0.6.1...v0.6.2) (2024-03-19)


### New Features and Enhancements

* Support `additionalProperties` of type any in Python and TS (box/box-codegen[#453](https://github.com/box/box-codegen/issues/453)) ([#82](https://github.com/box/box-codegen/issues/82)) ([dfe7ef0](https://github.com/box/box-codegen/commit/dfe7ef02e47ec74da72b375d0b201df4bb9e68fc))
* use getDiscriminatorsForUnion in generic serialization (box/box-codegen[#448](https://github.com/box/box-codegen/issues/448)) ([#81](https://github.com/box/box-codegen/issues/81)) ([2bb15a8](https://github.com/box/box-codegen/commit/2bb15a8067d568a5d8699f73a2d808e8049e832f))
* Update `outcomes` parameter of `StartWorkflow` (box/box-openapi[#413](https://github.com/box/box-codegen/issues/413)) ([#88](https://github.com/box/box-codegen/issues/88)) ([238216f](https://github.com/box/box-codegen/commit/238216fa55be53c4f27e14e8807be389b2d5605a))
