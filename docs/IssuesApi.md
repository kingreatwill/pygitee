# gitee.IssuesApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_repos_owner_repo_issues_comments_id**](IssuesApi.md#delete_v5_repos_owner_repo_issues_comments_id) | **DELETE** /v5/repos/{owner}/{repo}/issues/comments/{id} | 删除Issue某条评论
[**get_v5_enterprises_enterprise_issues**](IssuesApi.md#get_v5_enterprises_enterprise_issues) | **GET** /v5/enterprises/{enterprise}/issues | 获取某个企业的所有Issues
[**get_v5_enterprises_enterprise_issues_number**](IssuesApi.md#get_v5_enterprises_enterprise_issues_number) | **GET** /v5/enterprises/{enterprise}/issues/{number} | 获取企业的某个Issue
[**get_v5_enterprises_enterprise_issues_number_comments**](IssuesApi.md#get_v5_enterprises_enterprise_issues_number_comments) | **GET** /v5/enterprises/{enterprise}/issues/{number}/comments | 获取企业某个Issue所有评论
[**get_v5_enterprises_enterprise_issues_number_labels**](IssuesApi.md#get_v5_enterprises_enterprise_issues_number_labels) | **GET** /v5/enterprises/{enterprise}/issues/{number}/labels | 获取企业某个Issue所有标签
[**get_v5_issues**](IssuesApi.md#get_v5_issues) | **GET** /v5/issues | 获取当前授权用户的所有Issues
[**get_v5_orgs_org_issues**](IssuesApi.md#get_v5_orgs_org_issues) | **GET** /v5/orgs/{org}/issues | 获取当前用户某个组织的Issues
[**get_v5_repos_owner_issues_number_operate_logs**](IssuesApi.md#get_v5_repos_owner_issues_number_operate_logs) | **GET** /v5/repos/{owner}/issues/{number}/operate_logs | 获取某个Issue下的操作日志
[**get_v5_repos_owner_repo_issues**](IssuesApi.md#get_v5_repos_owner_repo_issues) | **GET** /v5/repos/{owner}/{repo}/issues | 仓库的所有Issues
[**get_v5_repos_owner_repo_issues_comments**](IssuesApi.md#get_v5_repos_owner_repo_issues_comments) | **GET** /v5/repos/{owner}/{repo}/issues/comments | 获取仓库所有Issue的评论
[**get_v5_repos_owner_repo_issues_comments_id**](IssuesApi.md#get_v5_repos_owner_repo_issues_comments_id) | **GET** /v5/repos/{owner}/{repo}/issues/comments/{id} | 获取仓库Issue某条评论
[**get_v5_repos_owner_repo_issues_number**](IssuesApi.md#get_v5_repos_owner_repo_issues_number) | **GET** /v5/repos/{owner}/{repo}/issues/{number} | 仓库的某个Issue
[**get_v5_repos_owner_repo_issues_number_comments**](IssuesApi.md#get_v5_repos_owner_repo_issues_number_comments) | **GET** /v5/repos/{owner}/{repo}/issues/{number}/comments | 获取仓库某个Issue所有的评论
[**get_v5_user_issues**](IssuesApi.md#get_v5_user_issues) | **GET** /v5/user/issues | 获取授权用户的所有Issues
[**patch_v5_repos_owner_issues_number**](IssuesApi.md#patch_v5_repos_owner_issues_number) | **PATCH** /v5/repos/{owner}/issues/{number} | 更新Issue
[**patch_v5_repos_owner_repo_issues_comments_id**](IssuesApi.md#patch_v5_repos_owner_repo_issues_comments_id) | **PATCH** /v5/repos/{owner}/{repo}/issues/comments/{id} | 更新Issue某条评论
[**post_v5_repos_owner_issues**](IssuesApi.md#post_v5_repos_owner_issues) | **POST** /v5/repos/{owner}/issues | 创建Issue
[**post_v5_repos_owner_repo_issues_number_comments**](IssuesApi.md#post_v5_repos_owner_repo_issues_number_comments) | **POST** /v5/repos/{owner}/{repo}/issues/{number}/comments | 创建某个Issue评论

# **delete_v5_repos_owner_repo_issues_comments_id**
> delete_v5_repos_owner_repo_issues_comments_id(owner, repo, id, access_token=access_token)

删除Issue某条评论

删除Issue某条评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除Issue某条评论
    api_instance.delete_v5_repos_owner_repo_issues_comments_id(owner, repo, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling IssuesApi->delete_v5_repos_owner_repo_issues_comments_id: %s\n" % e)
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

# **get_v5_enterprises_enterprise_issues**
> list[Issue] get_v5_enterprises_enterprise_issues(enterprise, access_token=access_token, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at, milestone=milestone, assignee=assignee, creator=creator, program=program)

获取某个企业的所有Issues

获取某个企业的所有Issues

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
state = 'open' # str | Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open (optional) (default to open)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
sort = 'created' # str | 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at (optional) (default to created)
direction = 'desc' # str | 排序方式: 升序(asc)，降序(desc)。默认: desc (optional) (default to desc)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
schedule = 'schedule_example' # str | 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 (optional)
deadline = 'deadline_example' # str | 计划截止日期，格式同上 (optional)
created_at = 'created_at_example' # str | 任务创建时间，格式同上 (optional)
finished_at = 'finished_at_example' # str | 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 (optional)
milestone = 'milestone_example' # str | 根据里程碑标题。none为没里程碑的，*为所有带里程碑的 (optional)
assignee = 'assignee_example' # str | 用户的username。 none为没指派者, *为所有带有指派者的 (optional)
creator = 'creator_example' # str | 创建Issues的用户username (optional)
program = 'program_example' # str | 所属项目名称。none为没所属有项目的，*为所有带所属项目的 (optional)

try:
    # 获取某个企业的所有Issues
    api_response = api_instance.get_v5_enterprises_enterprise_issues(enterprise, access_token=access_token, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at, milestone=milestone, assignee=assignee, creator=creator, program=program)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_enterprises_enterprise_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **state** | **str**| Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open | [optional] [default to open]
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **sort** | **str**| 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at | [optional] [default to created]
 **direction** | **str**| 排序方式: 升序(asc)，降序(desc)。默认: desc | [optional] [default to desc]
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **schedule** | **str**| 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 | [optional] 
 **deadline** | **str**| 计划截止日期，格式同上 | [optional] 
 **created_at** | **str**| 任务创建时间，格式同上 | [optional] 
 **finished_at** | **str**| 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 | [optional] 
 **milestone** | **str**| 根据里程碑标题。none为没里程碑的，*为所有带里程碑的 | [optional] 
 **assignee** | **str**| 用户的username。 none为没指派者, *为所有带有指派者的 | [optional] 
 **creator** | **str**| 创建Issues的用户username | [optional] 
 **program** | **str**| 所属项目名称。none为没所属有项目的，*为所有带所属项目的 | [optional] 

### Return type

[**list[Issue]**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_issues_number**
> Issue get_v5_enterprises_enterprise_issues_number(enterprise, number, access_token=access_token)

获取企业的某个Issue

获取企业的某个Issue

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取企业的某个Issue
    api_response = api_instance.get_v5_enterprises_enterprise_issues_number(enterprise, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_enterprises_enterprise_issues_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_issues_number_comments**
> list[Note] get_v5_enterprises_enterprise_issues_number_comments(enterprise, number, access_token=access_token, page=page, per_page=per_page)

获取企业某个Issue所有评论

获取企业某个Issue所有评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取企业某个Issue所有评论
    api_response = api_instance.get_v5_enterprises_enterprise_issues_number_comments(enterprise, number, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_enterprises_enterprise_issues_number_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Note]**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_issues_number_labels**
> list[Label] get_v5_enterprises_enterprise_issues_number_labels(enterprise, number, access_token=access_token, page=page, per_page=per_page)

获取企业某个Issue所有标签

获取企业某个Issue所有标签

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取企业某个Issue所有标签
    api_response = api_instance.get_v5_enterprises_enterprise_issues_number_labels(enterprise, number, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_enterprises_enterprise_issues_number_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
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

# **get_v5_issues**
> list[Issue] get_v5_issues(access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)

获取当前授权用户的所有Issues

获取当前授权用户的所有Issues

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
filter = 'assigned' # str | 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned (optional) (default to assigned)
state = 'open' # str | Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open (optional) (default to open)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
sort = 'created' # str | 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at (optional) (default to created)
direction = 'desc' # str | 排序方式: 升序(asc)，降序(desc)。默认: desc (optional) (default to desc)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
schedule = 'schedule_example' # str | 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 (optional)
deadline = 'deadline_example' # str | 计划截止日期，格式同上 (optional)
created_at = 'created_at_example' # str | 任务创建时间，格式同上 (optional)
finished_at = 'finished_at_example' # str | 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 (optional)

try:
    # 获取当前授权用户的所有Issues
    api_response = api_instance.get_v5_issues(access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **filter** | **str**| 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned | [optional] [default to assigned]
 **state** | **str**| Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open | [optional] [default to open]
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **sort** | **str**| 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at | [optional] [default to created]
 **direction** | **str**| 排序方式: 升序(asc)，降序(desc)。默认: desc | [optional] [default to desc]
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **schedule** | **str**| 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 | [optional] 
 **deadline** | **str**| 计划截止日期，格式同上 | [optional] 
 **created_at** | **str**| 任务创建时间，格式同上 | [optional] 
 **finished_at** | **str**| 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 | [optional] 

### Return type

[**list[Issue]**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_orgs_org_issues**
> list[Issue] get_v5_orgs_org_issues(org, access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)

获取当前用户某个组织的Issues

获取当前用户某个组织的Issues

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
filter = 'assigned' # str | 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned (optional) (default to assigned)
state = 'open' # str | Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open (optional) (default to open)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
sort = 'created' # str | 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at (optional) (default to created)
direction = 'desc' # str | 排序方式: 升序(asc)，降序(desc)。默认: desc (optional) (default to desc)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
schedule = 'schedule_example' # str | 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 (optional)
deadline = 'deadline_example' # str | 计划截止日期，格式同上 (optional)
created_at = 'created_at_example' # str | 任务创建时间，格式同上 (optional)
finished_at = 'finished_at_example' # str | 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 (optional)

try:
    # 获取当前用户某个组织的Issues
    api_response = api_instance.get_v5_orgs_org_issues(org, access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_orgs_org_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **filter** | **str**| 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned | [optional] [default to assigned]
 **state** | **str**| Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open | [optional] [default to open]
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **sort** | **str**| 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at | [optional] [default to created]
 **direction** | **str**| 排序方式: 升序(asc)，降序(desc)。默认: desc | [optional] [default to desc]
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **schedule** | **str**| 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 | [optional] 
 **deadline** | **str**| 计划截止日期，格式同上 | [optional] 
 **created_at** | **str**| 任务创建时间，格式同上 | [optional] 
 **finished_at** | **str**| 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 | [optional] 

### Return type

[**list[Issue]**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_issues_number_operate_logs**
> list[OperateLog] get_v5_repos_owner_issues_number_operate_logs(owner, number, access_token=access_token, repo=repo, sort=sort)

获取某个Issue下的操作日志

获取某个Issue下的操作日志

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)
repo = 'repo_example' # str | 仓库路径(path) (optional)
sort = 'desc' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional) (default to desc)

try:
    # 获取某个Issue下的操作日志
    api_response = api_instance.get_v5_repos_owner_issues_number_operate_logs(owner, number, access_token=access_token, repo=repo, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_repos_owner_issues_number_operate_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **repo** | **str**| 仓库路径(path) | [optional] 
 **sort** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] [default to desc]

### Return type

[**list[OperateLog]**](OperateLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_issues**
> list[Issue] get_v5_repos_owner_repo_issues(owner, repo, access_token=access_token, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at, milestone=milestone, assignee=assignee, creator=creator, program=program)

仓库的所有Issues

仓库的所有Issues

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
state = 'open' # str | Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open (optional) (default to open)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
sort = 'created' # str | 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at (optional) (default to created)
direction = 'desc' # str | 排序方式: 升序(asc)，降序(desc)。默认: desc (optional) (default to desc)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
schedule = 'schedule_example' # str | 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 (optional)
deadline = 'deadline_example' # str | 计划截止日期，格式同上 (optional)
created_at = 'created_at_example' # str | 任务创建时间，格式同上 (optional)
finished_at = 'finished_at_example' # str | 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 (optional)
milestone = 'milestone_example' # str | 根据里程碑标题。none为没里程碑的，*为所有带里程碑的 (optional)
assignee = 'assignee_example' # str | 用户的username。 none为没指派者, *为所有带有指派者的 (optional)
creator = 'creator_example' # str | 创建Issues的用户username (optional)
program = 'program_example' # str | 所属项目名称。none为没有所属项目，*为所有带所属项目的 (optional)

try:
    # 仓库的所有Issues
    api_response = api_instance.get_v5_repos_owner_repo_issues(owner, repo, access_token=access_token, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at, milestone=milestone, assignee=assignee, creator=creator, program=program)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_repos_owner_repo_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **state** | **str**| Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open | [optional] [default to open]
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **sort** | **str**| 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at | [optional] [default to created]
 **direction** | **str**| 排序方式: 升序(asc)，降序(desc)。默认: desc | [optional] [default to desc]
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **schedule** | **str**| 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 | [optional] 
 **deadline** | **str**| 计划截止日期，格式同上 | [optional] 
 **created_at** | **str**| 任务创建时间，格式同上 | [optional] 
 **finished_at** | **str**| 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 | [optional] 
 **milestone** | **str**| 根据里程碑标题。none为没里程碑的，*为所有带里程碑的 | [optional] 
 **assignee** | **str**| 用户的username。 none为没指派者, *为所有带有指派者的 | [optional] 
 **creator** | **str**| 创建Issues的用户username | [optional] 
 **program** | **str**| 所属项目名称。none为没有所属项目，*为所有带所属项目的 | [optional] 

### Return type

[**list[Issue]**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_issues_comments**
> Note get_v5_repos_owner_repo_issues_comments(owner, repo, access_token=access_token, sort=sort, direction=direction, since=since, page=page, per_page=per_page)

获取仓库所有Issue的评论

获取仓库所有Issue的评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'created' # str | Either created or updated. Default: created (optional) (default to created)
direction = 'asc' # str | Either asc or desc. Ignored without the sort parameter. (optional) (default to asc)
since = 'since_example' # str | Only comments updated at or after this time are returned.                                               This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 获取仓库所有Issue的评论
    api_response = api_instance.get_v5_repos_owner_repo_issues_comments(owner, repo, access_token=access_token, sort=sort, direction=direction, since=since, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_repos_owner_repo_issues_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **sort** | **str**| Either created or updated. Default: created | [optional] [default to created]
 **direction** | **str**| Either asc or desc. Ignored without the sort parameter. | [optional] [default to asc]
 **since** | **str**| Only comments updated at or after this time are returned.                                               This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_issues_comments_id**
> Note get_v5_repos_owner_repo_issues_comments_id(owner, repo, id, access_token=access_token)

获取仓库Issue某条评论

获取仓库Issue某条评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取仓库Issue某条评论
    api_response = api_instance.get_v5_repos_owner_repo_issues_comments_id(owner, repo, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_repos_owner_repo_issues_comments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **id** | **int**| 评论的ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_issues_number**
> Issue get_v5_repos_owner_repo_issues_number(owner, repo, number, access_token=access_token)

仓库的某个Issue

仓库的某个Issue

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 仓库的某个Issue
    api_response = api_instance.get_v5_repos_owner_repo_issues_number(owner, repo, number, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_repos_owner_repo_issues_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_issues_number_comments**
> Note get_v5_repos_owner_repo_issues_number_comments(owner, repo, number, access_token=access_token, since=since, page=page, per_page=per_page, order=order)

获取仓库某个Issue所有的评论

获取仓库某个Issue所有的评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str | 用户授权码 (optional)
since = 'since_example' # str | Only comments updated at or after this time are returned.                                               This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
order = 'asc' # str | 排序顺序: asc(default),desc (optional) (default to asc)

try:
    # 获取仓库某个Issue所有的评论
    api_response = api_instance.get_v5_repos_owner_repo_issues_number_comments(owner, repo, number, access_token=access_token, since=since, page=page, per_page=per_page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_repos_owner_repo_issues_number_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **since** | **str**| Only comments updated at or after this time are returned.                                               This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **order** | **str**| 排序顺序: asc(default),desc | [optional] [default to asc]

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_issues**
> list[Issue] get_v5_user_issues(access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)

获取授权用户的所有Issues

获取授权用户的所有Issues

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
filter = 'assigned' # str | 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned (optional) (default to assigned)
state = 'open' # str | Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open (optional) (default to open)
labels = 'labels_example' # str | 用逗号分开的标签。如: bug,performance (optional)
sort = 'created' # str | 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at (optional) (default to created)
direction = 'desc' # str | 排序方式: 升序(asc)，降序(desc)。默认: desc (optional) (default to desc)
since = 'since_example' # str | 起始的更新时间，要求时间格式为 ISO 8601 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
schedule = 'schedule_example' # str | 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 (optional)
deadline = 'deadline_example' # str | 计划截止日期，格式同上 (optional)
created_at = 'created_at_example' # str | 任务创建时间，格式同上 (optional)
finished_at = 'finished_at_example' # str | 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 (optional)

try:
    # 获取授权用户的所有Issues
    api_response = api_instance.get_v5_user_issues(access_token=access_token, filter=filter, state=state, labels=labels, sort=sort, direction=direction, since=since, page=page, per_page=per_page, schedule=schedule, deadline=deadline, created_at=created_at, finished_at=finished_at)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_v5_user_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **filter** | **str**| 筛选参数: 授权用户负责的(assigned)，授权用户创建的(created)，包含前两者的(all)。默认: assigned | [optional] [default to assigned]
 **state** | **str**| Issue的状态: open（开启的）, progressing(进行中), closed（关闭的）, rejected（拒绝的）。 默认: open | [optional] [default to open]
 **labels** | **str**| 用逗号分开的标签。如: bug,performance | [optional] 
 **sort** | **str**| 排序依据: 创建时间(created)，更新时间(updated_at)。默认: created_at | [optional] [default to created]
 **direction** | **str**| 排序方式: 升序(asc)，降序(desc)。默认: desc | [optional] [default to desc]
 **since** | **str**| 起始的更新时间，要求时间格式为 ISO 8601 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **schedule** | **str**| 计划开始日期，格式：20181006T173008+80-20181007T173008+80（区间），或者 -20181007T173008+80（小于20181007T173008+80），或者 20181006T173008+80-（大于20181006T173008+80），要求时间格式为20181006T173008+80 | [optional] 
 **deadline** | **str**| 计划截止日期，格式同上 | [optional] 
 **created_at** | **str**| 任务创建时间，格式同上 | [optional] 
 **finished_at** | **str**| 任务完成时间，即任务最后一次转为已完成状态的时间点。格式同上 | [optional] 

### Return type

[**list[Issue]**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_issues_number**
> Issue patch_v5_repos_owner_issues_number(owner, number, access_token=access_token, repo=repo, title=title, state=state, body=body, assignee=assignee, collaborators=collaborators, milestone=milestone, labels=labels, program=program, security_hole=security_hole)

更新Issue

更新Issue

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)
access_token = 'access_token_example' # str |  (optional)
repo = 'repo_example' # str |  (optional)
title = 'title_example' # str |  (optional)
state = 'state_example' # str |  (optional)
body = 'body_example' # str |  (optional)
assignee = 'assignee_example' # str |  (optional)
collaborators = 'collaborators_example' # str |  (optional)
milestone = 56 # int |  (optional)
labels = 'labels_example' # str |  (optional)
program = 'program_example' # str |  (optional)
security_hole = true # bool |  (optional)

try:
    # 更新Issue
    api_response = api_instance.patch_v5_repos_owner_issues_number(owner, number, access_token=access_token, repo=repo, title=title, state=state, body=body, assignee=assignee, collaborators=collaborators, milestone=milestone, labels=labels, program=program, security_hole=security_hole)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->patch_v5_repos_owner_issues_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 
 **access_token** | **str**|  | [optional] 
 **repo** | **str**|  | [optional] 
 **title** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **body** | **str**|  | [optional] 
 **assignee** | **str**|  | [optional] 
 **collaborators** | **str**|  | [optional] 
 **milestone** | **int**|  | [optional] 
 **labels** | **str**|  | [optional] 
 **program** | **str**|  | [optional] 
 **security_hole** | **bool**|  | [optional] 

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_repos_owner_repo_issues_comments_id**
> Note patch_v5_repos_owner_repo_issues_comments_id(access_token, body, owner, repo, id)

更新Issue某条评论

更新Issue某条评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
access_token = 'access_token_example' # str | 
body = 'body_example' # str | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
id = 56 # int | 评论的ID

try:
    # 更新Issue某条评论
    api_response = api_instance.patch_v5_repos_owner_repo_issues_comments_id(access_token, body, owner, repo, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->patch_v5_repos_owner_repo_issues_comments_id: %s\n" % e)
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

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_issues**
> Issue post_v5_repos_owner_issues(body, owner)

创建Issue

创建Issue

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
body = gitee.Body6() # Body6 | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)

try:
    # 创建Issue
    api_response = api_instance.post_v5_repos_owner_issues(body, owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->post_v5_repos_owner_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_repos_owner_repo_issues_number_comments**
> Note post_v5_repos_owner_repo_issues_number_comments(body, owner, repo, number)

创建某个Issue评论

创建某个Issue评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.IssuesApi()
body = gitee.Body16() # Body16 | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
number = 'number_example' # str | Issue 编号(区分大小写，无需添加 # 号)

try:
    # 创建某个Issue评论
    api_response = api_instance.post_v5_repos_owner_repo_issues_number_comments(body, owner, repo, number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->post_v5_repos_owner_repo_issues_number_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body16**](Body16.md)|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **number** | **str**| Issue 编号(区分大小写，无需添加 # 号) | 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

