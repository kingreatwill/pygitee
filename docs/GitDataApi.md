# gitee.GitDataApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v5_repos_owner_repo_git_blobs_sha**](GitDataApi.md#get_v5_repos_owner_repo_git_blobs_sha) | **GET** /v5/repos/{owner}/{repo}/git/blobs/{sha} | 获取文件Blob
[**get_v5_repos_owner_repo_git_trees_sha**](GitDataApi.md#get_v5_repos_owner_repo_git_trees_sha) | **GET** /v5/repos/{owner}/{repo}/git/trees/{sha} | 获取目录Tree

# **get_v5_repos_owner_repo_git_blobs_sha**
> Blob get_v5_repos_owner_repo_git_blobs_sha(owner, repo, sha, access_token=access_token)

获取文件Blob

获取文件Blob

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GitDataApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
sha = 'sha_example' # str | 文件的 Blob SHA，可通过 [获取仓库具体路径下的内容] API 获取
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取文件Blob
    api_response = api_instance.get_v5_repos_owner_repo_git_blobs_sha(owner, repo, sha, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitDataApi->get_v5_repos_owner_repo_git_blobs_sha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **sha** | **str**| 文件的 Blob SHA，可通过 [获取仓库具体路径下的内容] API 获取 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Blob**](Blob.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_git_trees_sha**
> Tree get_v5_repos_owner_repo_git_trees_sha(owner, repo, sha, access_token=access_token, recursive=recursive)

获取目录Tree

获取目录Tree

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.GitDataApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
sha = 'sha_example' # str | 可以是分支名(如master)、Commit或者目录Tree的SHA值
access_token = 'access_token_example' # str | 用户授权码 (optional)
recursive = 56 # int | 赋值为1递归获取目录 (optional)

try:
    # 获取目录Tree
    api_response = api_instance.get_v5_repos_owner_repo_git_trees_sha(owner, repo, sha, access_token=access_token, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GitDataApi->get_v5_repos_owner_repo_git_trees_sha: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **sha** | **str**| 可以是分支名(如master)、Commit或者目录Tree的SHA值 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **recursive** | **int**| 赋值为1递归获取目录 | [optional] 

### Return type

[**Tree**](Tree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

