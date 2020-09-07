# Body25

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | 用户授权码 | [optional] 
**title** | **str** | 必填。Pull Request 标题 | 
**head** | **str** | 必填。Pull Request 提交的源分支。格式：branch 或者：username:branch | 
**base** | **str** | 必填。Pull Request 提交目标分支的名称 | 
**body** | **str** | 可选。Pull Request 内容 | [optional] 
**milestone_number** | **int** | 可选。里程碑序号(id) | [optional] 
**labels** | **str** | 用逗号分开的标签，名称要求长度在 2-20 之间且非特殊字符。如: bug,performance | [optional] 
**issue** | **str** | 可选。Pull Request的标题和内容可以根据指定的Issue Id自动填充 | [optional] 
**assignees** | **str** | 可选。审查人员username，可多个，半角逗号分隔，如：(username1,username2), 注意: 当仓库代码审查设置中已设置【指派审查人员】则此选项无效 | [optional] 
**testers** | **str** | 可选。测试人员username，可多个，半角逗号分隔，如：(username1,username2), 注意: 当仓库代码审查设置中已设置【指派测试人员】则此选项无效 | [optional] 
**prune_source_branch** | **bool** | 可选。合并PR后是否删除源分支，默认false（不删除） | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

