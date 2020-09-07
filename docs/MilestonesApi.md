# gitee.MilestonesApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_repos_owner_repo_milestones_number**](MilestonesApi.md#delete_v5_repos_owner_repo_milestones_number) | **DELETE** /v5/repos/{owner}/{repo}/milestones/{number} | 删除仓库单个里程碑
[**get_v5_repos_owner_repo_milestones**](MilestonesApi.md#get_v5_repos_owner_repo_milestones) | **GET** /v5/repos/{owner}/{repo}/milestones | 获取仓库所有里程碑
[**get_v5_repos_owner_repo_milestones_number**](MilestonesApi.md#get_v5_repos_owner_repo_milestones_number) | **GET** /v5/repos/{owner}/{repo}/milestones/{number} | 获取仓库单个里程碑
[**patch_v5_repos_owner_repo_milestones_number**](MilestonesApi.md#patch_v5_repos_owner_repo_milestones_number) | **PATCH** /v5/repos/{owner}/{repo}/milestones/{number} | 更新仓库里程碑
[**post_v5_repos_owner_repo_milestones**](MilestonesApi.md#post_v5_repos_owner_repo_milestones) | **POST** /v5/repos/{owner}/{repo}/milestones | 创建仓库里程碑

# **delete_v5_repos_owner_repo_milestones_number**
> delete_v5_repos_owner_repo_milestones_number(owner, repo, number, access_token=access_token)

删除仓库单个里程碑

删除仓库单个里程碑

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MilestonesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 里程碑序号(id)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除仓库单个里程碑
    api_instance.delete_v5_repos_owner_repo_milestones_number(owner, repo, number, access_token=access_token)
except ApiException as e:
    print("Exception when calling MilestonesApi->delete_v5_repos_owner_repo_milestones_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 里程碑序号(id) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_milestones**
> list[Milestone] get_v5_repos_owner_repo_milestones(owner, repo, access_token=access_token, state=state, sort=sort, direction=direction, page=page, per_page=per_page)

获取仓库所有里程碑

获取仓库所有里程碑

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MilestonesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
state = 'open' # str | 里程碑状态: open, closed, all。默认: open (optional) (default to open)
sort = 'due_on' # str | 排序方式: due_on (optional) (default to due_on)
direction = 'direction_example' # str | 升序(asc)或是降序(desc)。默认: asc (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取仓库所有里程碑
    api_response = api_instance.get_v5_repos_owner_repo_milestones(owner, repo, access_token=access_token, state=state, sort=sort, direction=direction, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MilestonesApi->get_v5_repos_owner_repo_milestones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **state** | **str**| 里程碑状态: open, closed, all。默认: open | [optional] [default to open]
 **sort** | **str**| 排序方式: due_on | [optional] [default to due_on]
 **direction** | **str**| 升序(asc)或是降序(desc)。默认: asc | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Milestone]**](Milestone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_milestones_number**
> Milestone get_v5_repos_owner_repo_milestones_number(owner, repo, number, access_token=access_token)

获取仓库单个里程碑

获取仓库单个里程碑

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MilestonesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 里程碑序号(id)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库单个里程碑
    api_response = api_instance.get_v5_repos_owner_repo_milestones_number(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MilestonesApi->get_v5_repos_owner_repo_milestones_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 里程碑序号(id) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Milestone**](Milestone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo_milestones_number**
> Milestone patch_v5_repos_owner_repo_milestones_number(access_token, title, state, description, due_on, owner, repo, number)

更新仓库里程碑

更新仓库里程碑

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MilestonesApi()
access_token = 'access_token_example' # str | 
title = 'title_example' # str | 
state = 'state_example' # str | 
description = 'description_example' # str | 
due_on = 'due_on_example' # str | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 56 # int | 里程碑序号(id)

try:
    # 更新仓库里程碑
    api_response = api_instance.patch_v5_repos_owner_repo_milestones_number(access_token, title, state, description, due_on, owner, repo, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MilestonesApi->patch_v5_repos_owner_repo_milestones_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **title** | **str**|  | 
 **state** | **str**|  | 
 **description** | **str**|  | 
 **due_on** | **str**|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **int**| 里程碑序号(id) | 

### Return type

[**Milestone**](Milestone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_milestones**
> Milestone post_v5_repos_owner_repo_milestones(body, owner, repo)

创建仓库里程碑

创建仓库里程碑

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.MilestonesApi()
body = gitee.Body12() # Body12 | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)

try:
    # 创建仓库里程碑
    api_response = api_instance.post_v5_repos_owner_repo_milestones(body, owner, repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MilestonesApi->post_v5_repos_owner_repo_milestones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body12**](Body12.md)|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 

### Return type

[**Milestone**](Milestone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

