# Body59

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
**public** | **int** | 仓库开源类型。0(私有), 1(外部开源), 2(内部开源)，注：与private互斥，以public为主。 | [optional] 
**private** | **bool** | 仓库公开或私有。默认: 公开(false)，注：与public互斥，以public为主。 | [optional] 
**auto_init** | **bool** | 值为true时则会用README初始化仓库。默认: 不初始化(false) | [optional] 
**gitignore_template** | **str** | Git Ingore模版 | [optional] 
**license_template** | **str** | License模版 | [optional] 
**path** | **str** | 仓库路径 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

