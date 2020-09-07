# Body27

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | 用户授权码 | [optional] 
**merge_method** | **str** | 可选。合并PR的方法，merge（合并所有提交）和 squash（扁平化分支合并）。默认为merge。 | [optional] [default to 'merge']
**prune_source_branch** | **bool** | 可选。合并PR后是否删除源分支，默认false（不删除） | [optional] 
**title** | **str** | 可选。合并标题，默认为PR的标题 | [optional] 
**description** | **str** | 可选。合并描述，默认为 \&quot;Merge pull request !{pr_id} from {author}/{source_branch}\&quot;，与页面显示的默认一致。 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

