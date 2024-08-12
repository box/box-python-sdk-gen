# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## [1.3.0](https://github.com/box/box-codegen/compare/v1.2.0...v1.3.0) (2024-08-12)


### Bug Fixes

* Fix fetch method for multipart request (box/box-codegen[#545](https://github.com/box/box-codegen/issues/545)) ([#266](https://github.com/box/box-codegen/issues/266)) ([08a0818](https://github.com/box/box-codegen/commit/08a0818995d64995c3e2720a459f9221c9ca1dea))


### New Features and Enhancements

* parametrise chunked uploads endpoint urls (box/box-openapi[#444](https://github.com/box/box-codegen/issues/444)) ([#264](https://github.com/box/box-codegen/issues/264)) ([b5bce24](https://github.com/box/box-codegen/commit/b5bce24478c70ae6bb997adc773a0e2a76223568))

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
