# gitee.SearchApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v5_search_issues**](SearchApi.md#get_v5_search_issues) | **GET** /v5/search/issues | 搜索 Issues
[**get_v5_search_repositories**](SearchApi.md#get_v5_search_repositories) | **GET** /v5/search/repositories | 搜索仓库
[**get_v5_search_users**](SearchApi.md#get_v5_search_users) | **GET** /v5/search/users | 搜索用户

# **get_v5_search_issues**
> list[Issue] get_v5_search_issues(q, access_token=access_token, page=page, per_page=per_page, repo=repo, language=language, label=label, state=state, author=author, assignee=assignee, sort=sort, order=order)

搜索 Issues

搜索 Issues

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.SearchApi()
q = 'q_example' # str | 搜索关键字
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
repo = 'repo_example' # str | 筛选指定仓库 (path, e.g. oschina/git-osc) 的 issues (optional)
language = 'language_example' # str | 筛选指定语言的 issues (optional)
label = 'label_example' # str | 筛选指定标签的 issues (optional)
state = 'state_example' # str | 筛选指定状态的 issues, open(开启)、closed(完成)、rejected(拒绝) (optional)
author = 'author_example' # str | 筛选指定创建者 (username/login) 的 issues (optional)
assignee = 'assignee_example' # str | 筛选指定负责人 (username/login) 的 issues (optional)
sort = 'sort_example' # str | 排序字段，created_at(创建时间)、last_push_at(更新时间)、notes_count(评论数)，默认为最佳匹配 (optional)
order = 'desc' # str | 排序顺序: desc(default)、asc (optional) (default to desc)

try:
    # 搜索 Issues
    api_response = api_instance.get_v5_search_issues(q, access_token=access_token, page=page, per_page=per_page, repo=repo, language=language, label=label, state=state, author=author, assignee=assignee, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_v5_search_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| 搜索关键字 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **repo** | **str**| 筛选指定仓库 (path, e.g. oschina/git-osc) 的 issues | [optional] 
 **language** | **str**| 筛选指定语言的 issues | [optional] 
 **label** | **str**| 筛选指定标签的 issues | [optional] 
 **state** | **str**| 筛选指定状态的 issues, open(开启)、closed(完成)、rejected(拒绝) | [optional] 
 **author** | **str**| 筛选指定创建者 (username/login) 的 issues | [optional] 
 **assignee** | **str**| 筛选指定负责人 (username/login) 的 issues | [optional] 
 **sort** | **str**| 排序字段，created_at(创建时间)、last_push_at(更新时间)、notes_count(评论数)，默认为最佳匹配 | [optional] 
 **order** | **str**| 排序顺序: desc(default)、asc | [optional] [default to desc]

### Return type

[**list[Issue]**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_search_repositories**
> list[Project] get_v5_search_repositories(q, access_token=access_token, page=page, per_page=per_page, owner=owner, fork=fork, language=language, sort=sort, order=order)

搜索仓库

搜索仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.SearchApi()
q = 'q_example' # str | 搜索关键字
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
owner = 'owner_example' # str | 筛选指定空间地址(企业、组织或个人的地址 path) 的仓库 (optional)
fork = true # bool | 是否搜索含 fork 的仓库，默认：否 (optional)
language = 'language_example' # str | 筛选指定语言的仓库 (optional)
sort = 'sort_example' # str | 排序字段，last_push_at(更新时间)、stars_count(收藏数)、forks_count(Fork 数)、watches_count(关注数)，默认为最佳匹配 (optional)
order = 'desc' # str | 排序顺序: desc(default)、asc (optional) (default to desc)

try:
    # 搜索仓库
    api_response = api_instance.get_v5_search_repositories(q, access_token=access_token, page=page, per_page=per_page, owner=owner, fork=fork, language=language, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_v5_search_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| 搜索关键字 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **owner** | **str**| 筛选指定空间地址(企业、组织或个人的地址 path) 的仓库 | [optional] 
 **fork** | **bool**| 是否搜索含 fork 的仓库，默认：否 | [optional] 
 **language** | **str**| 筛选指定语言的仓库 | [optional] 
 **sort** | **str**| 排序字段，last_push_at(更新时间)、stars_count(收藏数)、forks_count(Fork 数)、watches_count(关注数)，默认为最佳匹配 | [optional] 
 **order** | **str**| 排序顺序: desc(default)、asc | [optional] [default to desc]

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_search_users**
> list[User] get_v5_search_users(q, access_token=access_token, page=page, per_page=per_page, sort=sort, order=order)

搜索用户

搜索用户

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.SearchApi()
q = 'q_example' # str | 搜索关键字
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
sort = 'sort_example' # str | 排序字段，joined_at(注册时间)，默认为最佳匹配 (optional)
order = 'desc' # str | 排序顺序: desc(default)、asc (optional) (default to desc)

try:
    # 搜索用户
    api_response = api_instance.get_v5_search_users(q, access_token=access_token, page=page, per_page=per_page, sort=sort, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_v5_search_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| 搜索关键字 | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **sort** | **str**| 排序字段，joined_at(注册时间)，默认为最佳匹配 | [optional] 
 **order** | **str**| 排序顺序: desc(default)、asc | [optional] [default to desc]

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

