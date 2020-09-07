# Body65

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | 用户授权码 | [optional] 
**name** | **str** | 仓库名称 | 
**description** | **str** | 仓库描述 | [optional] 
**homepage** | **str** | 主页(eg: https://gitee.com) | [optional] 
**has_issues** | **bool** | 允许提Issue与否。默认: 允许(true) | [optional] [default to True]
**has_wiki** | **bool** | 提供Wiki与否。默认: 提供(true) | [optional] [default to True]
**can_comment** | **bool** | 允许用户对仓库进行评论。默认： 允许(true) | [optional] [default to True]
**auto_init** | **bool** | 值为true时则会用README初始化仓库。默认: 不初始化(false) | [optional] 
**gitignore_template** | **str** | Git Ingore模版 | [optional] 
**license_template** | **str** | License模版 | [optional] 
**path** | **str** | 仓库路径 | [optional] 
**private** | **int** | 仓库开源类型。0(私有), 1(外部开源), 2(内部开源)。默认: 0 | [optional] [default to PrivateEnum._0]
**outsourced** | **bool** | 值为true值为外包仓库, false值为内部仓库。默认: 内部仓库(false) | [optional] 
**project_creator** | **str** | 负责人的username | [optional] 
**members** | **str** | 用逗号分开的仓库成员。如: member1,member2 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

