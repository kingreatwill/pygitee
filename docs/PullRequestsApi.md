# gitee.PullRequestsApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_repos_owner_repo_pulls_comments_id**](PullRequestsApi.md#delete_v5_repos_owner_repo_pulls_comments_id) | **DELETE** /v5/repos/{owner}/{repo}/pulls/comments/{id} | 删除评论
[**delete_v5_repos_owner_repo_pulls_number_assignees**](PullRequestsApi.md#delete_v5_repos_owner_repo_pulls_number_assignees) | **DELETE** /v5/repos/{owner}/{repo}/pulls/{number}/assignees | 取消用户审查 Pull Request
[**delete_v5_repos_owner_repo_pulls_number_labels_name**](PullRequestsApi.md#delete_v5_repos_owner_repo_pulls_number_labels_name) | **DELETE** /v5/repos/{owner}/{repo}/pulls/{number}/labels/{name} | 删除 Pull Request 标签
[**delete_v5_repos_owner_repo_pulls_number_testers**](PullRequestsApi.md#delete_v5_repos_owner_repo_pulls_number_testers) | **DELETE** /v5/repos/{owner}/{repo}/pulls/{number}/testers | 取消用户测试 Pull Request
[**get_v5_repos_owner_repo_pulls**](PullRequestsApi.md#get_v5_repos_owner_repo_pulls) | **GET** /v5/repos/{owner}/{repo}/pulls | 获取Pull Request列表
[**get_v5_repos_owner_repo_pulls_comments**](PullRequestsApi.md#get_v5_repos_owner_repo_pulls_comments) | **GET** /v5/repos/{owner}/{repo}/pulls/comments | 获取该仓库下的所有Pull Request评论
[**get_v5_repos_owner_repo_pulls_comments_id**](PullRequestsApi.md#get_v5_repos_owner_repo_pulls_comments_id) | **GET** /v5/repos/{owner}/{repo}/pulls/comments/{id} | 获取Pull Request的某个评论
[**get_v5_repos_owner_repo_pulls_number**](PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number) | **GET** /v5/repos/{owner}/{repo}/pulls/{number} | 获取单个Pull Request
[**get_v5_repos_owner_repo_pulls_number_comments**](PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_comments) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/comments | 获取某个Pull Request的所有评论
[**get_v5_repos_owner_repo_pulls_number_commits**](PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_commits) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/commits | 获取某Pull Request的所有Commit信息。最多显示250条Commit
[**get_v5_repos_owner_repo_pulls_number_files**](PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_files) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/files | Pull Request Commit文件列表。最多显示300条diff
[**get_v5_repos_owner_repo_pulls_number_issues**](PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_issues) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/issues | 获取 Pull Request 关联的 issues
[**get_v5_repos_owner_repo_pulls_number_labels**](PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_labels) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/labels | 获取某个 Pull Request 的所有标签
[**get_v5_repos_owner_repo_pulls_number_merge**](PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_merge) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/merge | 判断Pull Request是否已经合并
[**get_v5_repos_owner_repo_pulls_number_operate_logs**](PullRequestsApi.md#get_v5_repos_owner_repo_pulls_number_operate_logs) | **GET** /v5/repos/{owner}/{repo}/pulls/{number}/operate_logs | 获取某个Pull Request的操作日志
[**patch_v5_repos_owner_repo_pulls_comments_id**](PullRequestsApi.md#patch_v5_repos_owner_repo_pulls_comments_id) | **PATCH** /v5/repos/{owner}/{repo}/pulls/comments/{id} | 编辑评论
[**patch_v5_repos_owner_repo_pulls_number**](PullRequestsApi.md#patch_v5_repos_owner_repo_pulls_number) | **PATCH** /v5/repos/{owner}/{repo}/pulls/{number} | 更新Pull Request信息
[**patch_v5_repos_owner_repo_pulls_number_assignees**](PullRequestsApi.md#patch_v5_repos_owner_repo_pulls_number_assignees) | **PATCH** /v5/repos/{owner}/{repo}/pulls/{number}/assignees | 重置 Pull Request 审查 的状态
[**patch_v5_repos_owner_repo_pulls_number_testers**](PullRequestsApi.md#patch_v5_repos_owner_repo_pulls_number_testers) | **PATCH** /v5/repos/{owner}/{repo}/pulls/{number}/testers | 重置 Pull Request 测试 的状态
[**post_v5_repos_owner_repo_pulls**](PullRequestsApi.md#post_v5_repos_owner_repo_pulls) | **POST** /v5/repos/{owner}/{repo}/pulls | 创建Pull Request
[**post_v5_repos_owner_repo_pulls_number_assignees**](PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_assignees) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/assignees | 指派用户审查 Pull Request
[**post_v5_repos_owner_repo_pulls_number_comments**](PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_comments) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/comments | 提交Pull Request评论
[**post_v5_repos_owner_repo_pulls_number_labels**](PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_labels) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/labels | 创建 Pull Request 标签
[**post_v5_repos_owner_repo_pulls_number_review**](PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_review) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/review | 处理 Pull Request 审查
[**post_v5_repos_owner_repo_pulls_number_test**](PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_test) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/test | 处理 Pull Request 测试
[**post_v5_repos_owner_repo_pulls_number_testers**](PullRequestsApi.md#post_v5_repos_owner_repo_pulls_number_testers) | **POST** /v5/repos/{owner}/{repo}/pulls/{number}/testers | 指派用户测试 Pull Request
[**put_v5_repos_owner_repo_pulls_number_labels**](PullRequestsApi.md#put_v5_repos_owner_repo_pulls_number_labels) | **PUT** /v5/repos/{owner}/{repo}/pulls/{number}/labels | 替换 Pull Request 所有标签
[**put_v5_repos_owner_repo_pulls_number_merge**](PullRequestsApi.md#put_v5_repos_owner_repo_pulls_number_merge) | **PUT** /v5/repos/{owner}/{repo}/pulls/{number}/merge | 合并Pull Request

# **delete_v5_repos_owner_repo_pulls_comments_id**
> delete_v5_repos_owner_repo_pulls_comments_id(owner, repo, id, access_token=access_token)

删除评论

删除评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除评论
    api_instance.delete_v5_repos_owner_repo_pulls_comments_id(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling PullRequestsApi->delete_v5_repos_owner_repo_pulls_comments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_pulls_number_assignees**
> PullRequest delete_v5_repos_owner_repo_pulls_number_assignees(owner, repo, number, assignees, access_token=access_token)

取消用户审查 Pull Request

取消用户审查 Pull Request

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
assignees = 'assignees_example' # str | 用户的个人空间地址, 以 , 分隔
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消用户审查 Pull Request
    api_response = api_instance.delete_v5_repos_owner_repo_pulls_number_assignees(owner, repo, number, assignees, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->delete_v5_repos_owner_repo_pulls_number_assignees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **assignees** | **str**| 用户的个人空间地址, 以 , 分隔 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_pulls_number_labels_name**
> delete_v5_repos_owner_repo_pulls_number_labels_name(owner, repo, number, name, access_token=access_token)

删除 Pull Request 标签

删除 Pull Request 标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
name = 'name_example' # str | 标签名称
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除 Pull Request 标签
    api_instance.delete_v5_repos_owner_repo_pulls_number_labels_name(owner, repo, number, name, access_token=access_token)
except ApiException as e:
    print("Exception when calling PullRequestsApi->delete_v5_repos_owner_repo_pulls_number_labels_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **name** | **str**| 标签名称 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_repos_owner_repo_pulls_number_testers**
> PullRequest delete_v5_repos_owner_repo_pulls_number_testers(owner, repo, number, testers, access_token=access_token)

取消用户测试 Pull Request

取消用户测试 Pull Request

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
testers = 'testers_example' # str | 用户的个人空间地址, 以 , 分隔
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消用户测试 Pull Request
    api_response = api_instance.delete_v5_repos_owner_repo_pulls_number_testers(owner, repo, number, testers, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->delete_v5_repos_owner_repo_pulls_number_testers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **testers** | **str**| 用户的个人空间地址, 以 , 分隔 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pulls**
> list[PullRequest] get_v5_repos_owner_repo_pulls(owner, repo, access_token=access_token, state=state, head=head, base=base, sort=sort, direction=direction, milestone_number=milestone_number, labels=labels, page=page, per_page=per_page)

获取Pull Request列表

获取Pull Request列表

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
state = 'open' # str | 可选。Pull Request 状态 (optional) (default to open)
head = 'head_example' # str | 可选。Pull Request 提交的源分支。格式：branch 或者：username:branch (optional)
base = 'base_example' # str | 可选。Pull Request 提交目标分支的名称。 (optional)
sort = 'created' # str | 可选。排序字段，默认按创建时间 (optional) (default to created)
direction = 'desc' # str | 可选。升序/降序 (optional) (default to desc)
milestone_number = 56 # int | 可选。里程碑序号(id) (optional)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取Pull Request列表
    api_response = api_instance.get_v5_repos_owner_repo_pulls(owner, repo, access_token=access_token, state=state, head=head, base=base, sort=sort, direction=direction, milestone_number=milestone_number, labels=labels, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->get_v5_repos_owner_repo_pulls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **state** | **str**| 可选。Pull Request 状态 | [optional] [default to open]
 **head** | **str**| 可选。Pull Request 提交的源分支。格式：branch 或者：username:branch | [optional] 
 **base** | **str**| 可选。Pull Request 提交目标分支的名称。 | [optional] 
 **sort** | **str**| 可选。排序字段，默认按创建时间 | [optional] [default to created]
 **direction** | **str**| 可选。升序/降序 | [optional] [default to desc]
 **milestone_number** | **int**| 可选。里程碑序号(id) | [optional] 
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[PullRequest]**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pulls_comments**
> list[PullRequestComments] get_v5_repos_owner_repo_pulls_comments(owner, repo, access_token=access_token, sort=sort, direction=direction, since=since, page=page, per_page=per_page)

获取该仓库下的所有Pull Request评论

获取该仓库下的所有Pull Request评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'created' # str | 可选。按创建时间/更新时间排序 (optional) (default to created)
direction = 'desc' # str | 可选。升序/降序 (optional) (default to desc)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取该仓库下的所有Pull Request评论
    api_response = api_instance.get_v5_repos_owner_repo_pulls_comments(owner, repo, access_token=access_token, sort=sort, direction=direction, since=since, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->get_v5_repos_owner_repo_pulls_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **sort** | **str**| 可选。按创建时间/更新时间排序 | [optional] [default to created]
 **direction** | **str**| 可选。升序/降序 | [optional] [default to desc]
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[PullRequestComments]**](PullRequestComments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pulls_comments_id**
> PullRequestComments get_v5_repos_owner_repo_pulls_comments_id(owner, repo, id, access_token=access_token)

获取Pull Request的某个评论

获取Pull Request的某个评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取Pull Request的某个评论
    api_response = api_instance.get_v5_repos_owner_repo_pulls_comments_id(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->get_v5_repos_owner_repo_pulls_comments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**|  | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**PullRequestComments**](PullRequestComments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pulls_number**
> PullRequest get_v5_repos_owner_repo_pulls_number(owner, repo, number, access_token=access_token)

获取单个Pull Request

获取单个Pull Request

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取单个Pull Request
    api_response = api_instance.get_v5_repos_owner_repo_pulls_number(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->get_v5_repos_owner_repo_pulls_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pulls_number_comments**
> list[PullRequestComments] get_v5_repos_owner_repo_pulls_number_comments(owner, repo, number, access_token=access_token, page=page, per_page=per_page)

获取某个Pull Request的所有评论

获取某个Pull Request的所有评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取某个Pull Request的所有评论
    api_response = api_instance.get_v5_repos_owner_repo_pulls_number_comments(owner, repo, number, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->get_v5_repos_owner_repo_pulls_number_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[PullRequestComments]**](PullRequestComments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pulls_number_commits**
> list[PullRequestCommits] get_v5_repos_owner_repo_pulls_number_commits(owner, repo, number, access_token=access_token)

获取某Pull Request的所有Commit信息。最多显示250条Commit

获取某Pull Request的所有Commit信息。最多显示250条Commit

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取某Pull Request的所有Commit信息。最多显示250条Commit
    api_response = api_instance.get_v5_repos_owner_repo_pulls_number_commits(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->get_v5_repos_owner_repo_pulls_number_commits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**list[PullRequestCommits]**](PullRequestCommits.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pulls_number_files**
> list[PullRequestFiles] get_v5_repos_owner_repo_pulls_number_files(owner, repo, number, access_token=access_token)

Pull Request Commit文件列表。最多显示300条diff

Pull Request Commit文件列表。最多显示300条diff

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # Pull Request Commit文件列表。最多显示300条diff
    api_response = api_instance.get_v5_repos_owner_repo_pulls_number_files(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->get_v5_repos_owner_repo_pulls_number_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**list[PullRequestFiles]**](PullRequestFiles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pulls_number_issues**
> list[Issue] get_v5_repos_owner_repo_pulls_number_issues(owner, repo, number, access_token=access_token, page=page, per_page=per_page)

获取 Pull Request 关联的 issues

获取 Pull Request 关联的 issues

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取 Pull Request 关联的 issues
    api_response = api_instance.get_v5_repos_owner_repo_pulls_number_issues(owner, repo, number, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->get_v5_repos_owner_repo_pulls_number_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**|  | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Issue]**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pulls_number_labels**
> list[Label] get_v5_repos_owner_repo_pulls_number_labels(owner, repo, number, access_token=access_token, page=page, per_page=per_page)

获取某个 Pull Request 的所有标签

获取某个 Pull Request 的所有标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取某个 Pull Request 的所有标签
    api_response = api_instance.get_v5_repos_owner_repo_pulls_number_labels(owner, repo, number, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->get_v5_repos_owner_repo_pulls_number_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Label]**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pulls_number_merge**
> get_v5_repos_owner_repo_pulls_number_merge(owner, repo, number, access_token=access_token)

判断Pull Request是否已经合并

判断Pull Request是否已经合并

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 判断Pull Request是否已经合并
    api_instance.get_v5_repos_owner_repo_pulls_number_merge(owner, repo, number, access_token=access_token)
except ApiException as e:
    print("Exception when calling PullRequestsApi->get_v5_repos_owner_repo_pulls_number_merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_pulls_number_operate_logs**
> OperateLog get_v5_repos_owner_repo_pulls_number_operate_logs(owner, repo, number, access_token=access_token, sort=sort)

获取某个Pull Request的操作日志

获取某个Pull Request的操作日志

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'desc' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional) (default to desc)

try:
    # 获取某个Pull Request的操作日志
    api_response = api_instance.get_v5_repos_owner_repo_pulls_number_operate_logs(owner, repo, number, access_token=access_token, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->get_v5_repos_owner_repo_pulls_number_operate_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **sort** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] [default to desc]

### Return type

[**OperateLog**](OperateLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo_pulls_comments_id**
> PullRequestComments patch_v5_repos_owner_repo_pulls_comments_id(access_token, body, owner, repo, id)

编辑评论

编辑评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
access_token = 'access_token_example' # str | 
body = 'body_example' # str | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID

try:
    # 编辑评论
    api_response = api_instance.patch_v5_repos_owner_repo_pulls_comments_id(access_token, body, owner, repo, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->patch_v5_repos_owner_repo_pulls_comments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **body** | **str**|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 

### Return type

[**PullRequestComments**](PullRequestComments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo_pulls_number**
> PullRequest patch_v5_repos_owner_repo_pulls_number(owner, repo, number, access_token=access_token, title=title, body=body, state=state, milestone_number=milestone_number, labels=labels, assignees_number=assignees_number, testers_number=testers_number)

更新Pull Request信息

更新Pull Request信息

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str |  (optional)
title = 'title_example' # str |  (optional)
body = 'body_example' # str |  (optional)
state = 'state_example' # str |  (optional)
milestone_number = 56 # int |  (optional)
labels = 'labels_example' # str |  (optional)
assignees_number = 56 # int |  (optional)
testers_number = 56 # int |  (optional)

try:
    # 更新Pull Request信息
    api_response = api_instance.patch_v5_repos_owner_repo_pulls_number(owner, repo, number, access_token=access_token, title=title, body=body, state=state, milestone_number=milestone_number, labels=labels, assignees_number=assignees_number, testers_number=testers_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->patch_v5_repos_owner_repo_pulls_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **body** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **milestone_number** | **int**|  | [optional] 
 **labels** | **str**|  | [optional] 
 **assignees_number** | **int**|  | [optional] 
 **testers_number** | **int**|  | [optional] 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo_pulls_number_assignees**
> PullRequest patch_v5_repos_owner_repo_pulls_number_assignees(owner, repo, number, access_token=access_token, reset_all=reset_all)

重置 Pull Request 审查 的状态

重置 Pull Request 审查 的状态

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str |  (optional)
reset_all = true # bool |  (optional)

try:
    # 重置 Pull Request 审查 的状态
    api_response = api_instance.patch_v5_repos_owner_repo_pulls_number_assignees(owner, repo, number, access_token=access_token, reset_all=reset_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->patch_v5_repos_owner_repo_pulls_number_assignees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**|  | [optional] 
 **reset_all** | **bool**|  | [optional] 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo_pulls_number_testers**
> PullRequest patch_v5_repos_owner_repo_pulls_number_testers(owner, repo, number, access_token=access_token, reset_all=reset_all)

重置 Pull Request 测试 的状态

重置 Pull Request 测试 的状态

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
access_token = 'access_token_example' # str |  (optional)
reset_all = true # bool |  (optional)

try:
    # 重置 Pull Request 测试 的状态
    api_response = api_instance.patch_v5_repos_owner_repo_pulls_number_testers(owner, repo, number, access_token=access_token, reset_all=reset_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->patch_v5_repos_owner_repo_pulls_number_testers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **access_token** | **str**|  | [optional] 
 **reset_all** | **bool**|  | [optional] 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_pulls**
> PullRequest post_v5_repos_owner_repo_pulls(body, owner, repo)

创建Pull Request

创建Pull Request

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
body = gitee.Body25() # Body25 | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)

try:
    # 创建Pull Request
    api_response = api_instance.post_v5_repos_owner_repo_pulls(body, owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->post_v5_repos_owner_repo_pulls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body25**](Body25.md)|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_pulls_number_assignees**
> PullRequest post_v5_repos_owner_repo_pulls_number_assignees(body, owner, repo, number)

指派用户审查 Pull Request

指派用户审查 Pull Request

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
body = gitee.Body30() # Body30 | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数

try:
    # 指派用户审查 Pull Request
    api_response = api_instance.post_v5_repos_owner_repo_pulls_number_assignees(body, owner, repo, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->post_v5_repos_owner_repo_pulls_number_assignees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body30**](Body30.md)|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_pulls_number_comments**
> PullRequestComments post_v5_repos_owner_repo_pulls_number_comments(body, owner, repo, number)

提交Pull Request评论

提交Pull Request评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
body = gitee.Body34() # Body34 | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数

try:
    # 提交Pull Request评论
    api_response = api_instance.post_v5_repos_owner_repo_pulls_number_comments(body, owner, repo, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->post_v5_repos_owner_repo_pulls_number_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body34**](Body34.md)|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 

### Return type

[**PullRequestComments**](PullRequestComments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_pulls_number_labels**
> Label post_v5_repos_owner_repo_pulls_number_labels(owner, repo, number, body=body)

创建 Pull Request 标签

创建 Pull Request 标签  需要在请求的 body 里填上数组，元素为标签的名字。如: [\"performance\", \"bug\"]

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
body = gitee.Body36() # Body36 |  (optional)

try:
    # 创建 Pull Request 标签
    api_response = api_instance.post_v5_repos_owner_repo_pulls_number_labels(owner, repo, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->post_v5_repos_owner_repo_pulls_number_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **body** | [**Body36**](Body36.md)|  | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_pulls_number_review**
> post_v5_repos_owner_repo_pulls_number_review(owner, repo, number, body=body)

处理 Pull Request 审查

处理 Pull Request 审查

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
body = gitee.Body28() # Body28 |  (optional)

try:
    # 处理 Pull Request 审查
    api_instance.post_v5_repos_owner_repo_pulls_number_review(owner, repo, number, body=body)
except ApiException as e:
    print("Exception when calling PullRequestsApi->post_v5_repos_owner_repo_pulls_number_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **body** | [**Body28**](Body28.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_pulls_number_test**
> post_v5_repos_owner_repo_pulls_number_test(owner, repo, number, body=body)

处理 Pull Request 测试

处理 Pull Request 测试

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
body = gitee.Body29() # Body29 |  (optional)

try:
    # 处理 Pull Request 测试
    api_instance.post_v5_repos_owner_repo_pulls_number_test(owner, repo, number, body=body)
except ApiException as e:
    print("Exception when calling PullRequestsApi->post_v5_repos_owner_repo_pulls_number_test: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **body** | [**Body29**](Body29.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_pulls_number_testers**
> PullRequest post_v5_repos_owner_repo_pulls_number_testers(body, owner, repo, number)

指派用户测试 Pull Request

指派用户测试 Pull Request

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
body = gitee.Body32() # Body32 | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数

try:
    # 指派用户测试 Pull Request
    api_response = api_instance.post_v5_repos_owner_repo_pulls_number_testers(body, owner, repo, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->post_v5_repos_owner_repo_pulls_number_testers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body32**](Body32.md)|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_repos_owner_repo_pulls_number_labels**
> Label put_v5_repos_owner_repo_pulls_number_labels(owner, repo, number, body=body)

替换 Pull Request 所有标签

替换 Pull Request 所有标签  需要在请求的body里填上数组，元素为标签的名字。如: [\"performance\", \"bug\"]

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
body = gitee.Body35() # Body35 |  (optional)

try:
    # 替换 Pull Request 所有标签
    api_response = api_instance.put_v5_repos_owner_repo_pulls_number_labels(owner, repo, number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PullRequestsApi->put_v5_repos_owner_repo_pulls_number_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **body** | [**Body35**](Body35.md)|  | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_repos_owner_repo_pulls_number_merge**
> put_v5_repos_owner_repo_pulls_number_merge(owner, repo, number, body=body)

合并Pull Request

合并Pull Request

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.PullRequestsApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 第几个PR，即本仓库PR的序数
body = gitee.Body27() # Body27 |  (optional)

try:
    # 合并Pull Request
    api_instance.put_v5_repos_owner_repo_pulls_number_merge(owner, repo, number, body=body)
except ApiException as e:
    print("Exception when calling PullRequestsApi->put_v5_repos_owner_repo_pulls_number_merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 第几个PR，即本仓库PR的序数 | 
 **body** | [**Body27**](Body27.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

