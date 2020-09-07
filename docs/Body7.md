# Body7

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | 用户授权码 | [optional] 
**repo** | **str** | 仓库路径(path) | [optional] 
**title** | **str** | Issue标题 | [optional] 
**state** | **str** | Issue 状态，open（开启的）、progressing（进行中）、closed（关闭的） | [optional] 
**body** | **str** | Issue描述 | [optional] 
**assignee** | **str** | Issue负责人的个人空间地址 | [optional] 
**collaborators** | **str** | Issue协助者的个人空间地址, 以 , 分隔 | [optional] 
**milestone** | **int** | 里程碑序号 | [optional] 
**labels** | **str** | 用逗号分开的标签，名称要求长度在 2-20 之间且非特殊字符。如: bug,performance | [optional] 
**program** | **str** | 项目ID | [optional] 
**security_hole** | **bool** | 是否是私有issue(默认为false) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

