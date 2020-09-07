# Body40

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | 用户授权码 | [optional] 
**url** | **str** | 远程HTTP URL | 
**password** | **str** | 请求URL时会带上该密码，防止URL被恶意请求 | [optional] 
**push_events** | **bool** | Push代码到仓库 | [optional] [default to True]
**tag_push_events** | **bool** | 提交Tag到仓库 | [optional] 
**issues_events** | **bool** | 创建/关闭Issue | [optional] 
**note_events** | **bool** | 评论了Issue/代码等等 | [optional] 
**merge_requests_events** | **bool** | 合并请求和合并后 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

