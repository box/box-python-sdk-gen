# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

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
