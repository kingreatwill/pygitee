# Body19

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
**issue_comment** | **bool** | 允许对“关闭”状态的 Issue 进行评论。默认: 不允许(false) | [optional] 
**security_hole_enabled** | **bool** | 允许用户创建涉及敏感信息的 Issue。默认: 不允许(false) | [optional] 
**private** | **bool** | 仓库公开或私有。 | [optional] 
**path** | **str** | 更新仓库路径 | [optional] 
**default_branch** | **str** | 更新默认分支 | [optional] 
**pull_requests_enabled** | **bool** | 接受 pull request，协作开发 | [optional] 
**online_edit_enabled** | **bool** | 是否允许仓库文件在线编辑 | [optional] 
**lightweight_pr_enabled** | **bool** | 是否接受轻量级 pull request | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

