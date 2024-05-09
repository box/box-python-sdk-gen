# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

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
