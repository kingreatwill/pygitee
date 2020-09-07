# gitee.EnterprisesApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_enterprises_enterprise_members_username**](EnterprisesApi.md#delete_v5_enterprises_enterprise_members_username) | **DELETE** /v5/enterprises/{enterprise}/members/{username} | 移除企业成员
[**delete_v5_enterprises_enterprise_week_reports_report_id_comments_id**](EnterprisesApi.md#delete_v5_enterprises_enterprise_week_reports_report_id_comments_id) | **DELETE** /v5/enterprises/{enterprise}/week_reports/{report_id}/comments/{id} | 删除周报某个评论
[**get_v5_enterprise_enterprise_pull_requests**](EnterprisesApi.md#get_v5_enterprise_enterprise_pull_requests) | **GET** /v5/enterprise/{enterprise}/pull_requests | 企业Pull Reuqest 列表
[**get_v5_enterprises_enterprise**](EnterprisesApi.md#get_v5_enterprises_enterprise) | **GET** /v5/enterprises/{enterprise} | 获取一个企业
[**get_v5_enterprises_enterprise_members**](EnterprisesApi.md#get_v5_enterprises_enterprise_members) | **GET** /v5/enterprises/{enterprise}/members | 列出企业的所有成员
[**get_v5_enterprises_enterprise_members_username**](EnterprisesApi.md#get_v5_enterprises_enterprise_members_username) | **GET** /v5/enterprises/{enterprise}/members/{username} | 获取企业的一个成员
[**get_v5_enterprises_enterprise_users_username_week_reports**](EnterprisesApi.md#get_v5_enterprises_enterprise_users_username_week_reports) | **GET** /v5/enterprises/{enterprise}/users/{username}/week_reports | 个人周报列表
[**get_v5_enterprises_enterprise_week_reports**](EnterprisesApi.md#get_v5_enterprises_enterprise_week_reports) | **GET** /v5/enterprises/{enterprise}/week_reports | 企业成员周报列表
[**get_v5_enterprises_enterprise_week_reports_id**](EnterprisesApi.md#get_v5_enterprises_enterprise_week_reports_id) | **GET** /v5/enterprises/{enterprise}/week_reports/{id} | 周报详情
[**get_v5_enterprises_enterprise_week_reports_id_comments**](EnterprisesApi.md#get_v5_enterprises_enterprise_week_reports_id_comments) | **GET** /v5/enterprises/{enterprise}/week_reports/{id}/comments | 某个周报评论列表
[**get_v5_user_enterprises**](EnterprisesApi.md#get_v5_user_enterprises) | **GET** /v5/user/enterprises | 列出授权用户所属的企业
[**patch_v5_enterprises_enterprise_week_report_id**](EnterprisesApi.md#patch_v5_enterprises_enterprise_week_report_id) | **PATCH** /v5/enterprises/{enterprise}/week_report/{id} | 编辑周报
[**post_v5_enterprises_enterprise_members**](EnterprisesApi.md#post_v5_enterprises_enterprise_members) | **POST** /v5/enterprises/{enterprise}/members | 添加或邀请企业成员
[**post_v5_enterprises_enterprise_week_report**](EnterprisesApi.md#post_v5_enterprises_enterprise_week_report) | **POST** /v5/enterprises/{enterprise}/week_report | 新建周报
[**post_v5_enterprises_enterprise_week_reports_id_comment**](EnterprisesApi.md#post_v5_enterprises_enterprise_week_reports_id_comment) | **POST** /v5/enterprises/{enterprise}/week_reports/{id}/comment | 评论周报
[**put_v5_enterprises_enterprise_members_username**](EnterprisesApi.md#put_v5_enterprises_enterprise_members_username) | **PUT** /v5/enterprises/{enterprise}/members/{username} | 修改企业成员权限或备注

# **delete_v5_enterprises_enterprise_members_username**
> delete_v5_enterprises_enterprise_members_username(enterprise, username, access_token=access_token)

移除企业成员

移除企业成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 移除企业成员
    api_instance.delete_v5_enterprises_enterprise_members_username(enterprise, username, access_token=access_token)
except ApiException as e:
    print("Exception when calling EnterprisesApi->delete_v5_enterprises_enterprise_members_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_enterprises_enterprise_week_reports_report_id_comments_id**
> delete_v5_enterprises_enterprise_week_reports_report_id_comments_id(enterprise, report_id, id, access_token=access_token)

删除周报某个评论

删除周报某个评论

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
report_id = 56 # int | 周报ID
id = 56 # int | 评论ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 删除周报某个评论
    api_instance.delete_v5_enterprises_enterprise_week_reports_report_id_comments_id(enterprise, report_id, id, access_token=access_token)
except ApiException as e:
    print("Exception when calling EnterprisesApi->delete_v5_enterprises_enterprise_week_reports_report_id_comments_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **report_id** | **int**| 周报ID | 
 **id** | **int**| 评论ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprise_enterprise_pull_requests**
> list[PullRequest] get_v5_enterprise_enterprise_pull_requests(enterprise, access_token=access_token, issue_number=issue_number, repo=repo, program_id=program_id, state=state, head=head, base=base, sort=sort, direction=direction, milestone_number=milestone_number, labels=labels, page=page, per_page=per_page)

企业Pull Reuqest 列表

企业Pull Reuqest 列表

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
issue_number = 'issue_number_example' # str | 可选。Issue 编号(区分大小写，无需添加 # 号) (optional)
repo = 'repo_example' # str | 可选。仓库路径(path) (optional)
program_id = 56 # int | 可选。项目ID (optional)
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
    # 企业Pull Reuqest 列表
    api_response = api_instance.get_v5_enterprise_enterprise_pull_requests(enterprise, access_token=access_token, issue_number=issue_number, repo=repo, program_id=program_id, state=state, head=head, base=base, sort=sort, direction=direction, milestone_number=milestone_number, labels=labels, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->get_v5_enterprise_enterprise_pull_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **issue_number** | **str**| 可选。Issue 编号(区分大小写，无需添加 # 号) | [optional] 
 **repo** | **str**| 可选。仓库路径(path) | [optional] 
 **program_id** | **int**| 可选。项目ID | [optional] 
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

# **get_v5_enterprises_enterprise**
> EnterpriseBasic get_v5_enterprises_enterprise(enterprise, access_token=access_token)

获取一个企业

获取一个企业

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个企业
    api_response = api_instance.get_v5_enterprises_enterprise(enterprise, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->get_v5_enterprises_enterprise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**EnterpriseBasic**](EnterpriseBasic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_members**
> list[EnterpriseMember] get_v5_enterprises_enterprise_members(enterprise, access_token=access_token, role=role)

列出企业的所有成员

列出企业的所有成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
role = 'all' # str | 根据角色筛选成员 (optional) (default to all)

try:
    # 列出企业的所有成员
    api_response = api_instance.get_v5_enterprises_enterprise_members(enterprise, access_token=access_token, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->get_v5_enterprises_enterprise_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **role** | **str**| 根据角色筛选成员 | [optional] [default to all]

### Return type

[**list[EnterpriseMember]**](EnterpriseMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_members_username**
> EnterpriseMember get_v5_enterprises_enterprise_members_username(enterprise, username, access_token=access_token)

获取企业的一个成员

获取企业的一个成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取企业的一个成员
    api_response = api_instance.get_v5_enterprises_enterprise_members_username(enterprise, username, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->get_v5_enterprises_enterprise_members_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**EnterpriseMember**](EnterpriseMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_users_username_week_reports**
> list[WeekReport] get_v5_enterprises_enterprise_users_username_week_reports(enterprise, username, access_token=access_token, page=page, per_page=per_page)

个人周报列表

个人周报列表

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 个人周报列表
    api_response = api_instance.get_v5_enterprises_enterprise_users_username_week_reports(enterprise, username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->get_v5_enterprises_enterprise_users_username_week_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[WeekReport]**](WeekReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_week_reports**
> list[WeekReport] get_v5_enterprises_enterprise_week_reports(enterprise, access_token=access_token, page=page, per_page=per_page, username=username, year=year, week_index=week_index, _date=_date)

企业成员周报列表

企业成员周报列表

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
username = 'username_example' # str | 用户名(username/login) (optional)
year = 56 # int | 周报所属年 (optional)
week_index = 56 # int | 周报所属周 (optional)
_date = '_date_example' # str | 周报日期(格式：2019-03-25) (optional)

try:
    # 企业成员周报列表
    api_response = api_instance.get_v5_enterprises_enterprise_week_reports(enterprise, access_token=access_token, page=page, per_page=per_page, username=username, year=year, week_index=week_index, _date=_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->get_v5_enterprises_enterprise_week_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **username** | **str**| 用户名(username/login) | [optional] 
 **year** | **int**| 周报所属年 | [optional] 
 **week_index** | **int**| 周报所属周 | [optional] 
 **_date** | **str**| 周报日期(格式：2019-03-25) | [optional] 

### Return type

[**list[WeekReport]**](WeekReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_week_reports_id**
> WeekReport get_v5_enterprises_enterprise_week_reports_id(enterprise, id, access_token=access_token)

周报详情

周报详情

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
id = 56 # int | 周报ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 周报详情
    api_response = api_instance.get_v5_enterprises_enterprise_week_reports_id(enterprise, id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->get_v5_enterprises_enterprise_week_reports_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **id** | **int**| 周报ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**WeekReport**](WeekReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_enterprises_enterprise_week_reports_id_comments**
> list[Note] get_v5_enterprises_enterprise_week_reports_id_comments(enterprise, id, access_token=access_token, page=page, per_page=per_page)

某个周报评论列表

某个周报评论列表

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
id = 56 # int | 周报ID
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 某个周报评论列表
    api_response = api_instance.get_v5_enterprises_enterprise_week_reports_id_comments(enterprise, id, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->get_v5_enterprises_enterprise_week_reports_id_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **id** | **int**| 周报ID | 
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

# **get_v5_user_enterprises**
> list[EnterpriseBasic] get_v5_user_enterprises(access_token=access_token, page=page, per_page=per_page, admin=admin)

列出授权用户所属的企业

列出授权用户所属的企业

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
admin = true # bool | 只列出授权用户管理的企业 (optional) (default to true)

try:
    # 列出授权用户所属的企业
    api_response = api_instance.get_v5_user_enterprises(access_token=access_token, page=page, per_page=per_page, admin=admin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->get_v5_user_enterprises: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **admin** | **bool**| 只列出授权用户管理的企业 | [optional] [default to true]

### Return type

[**list[EnterpriseBasic]**](EnterpriseBasic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_enterprises_enterprise_week_report_id**
> WeekReport patch_v5_enterprises_enterprise_week_report_id(access_token, content, enterprise, id)

编辑周报

编辑周报

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
access_token = 'access_token_example' # str | 
content = 'content_example' # str | 
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
id = 56 # int | 周报ID

try:
    # 编辑周报
    api_response = api_instance.patch_v5_enterprises_enterprise_week_report_id(access_token, content, enterprise, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->patch_v5_enterprises_enterprise_week_report_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**|  | 
 **content** | **str**|  | 
 **enterprise** | **str**| 企业的路径(path/login) | 
 **id** | **int**| 周报ID | 

### Return type

[**WeekReport**](WeekReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_enterprises_enterprise_members**
> post_v5_enterprises_enterprise_members(enterprise, body=body)

添加或邀请企业成员

添加或邀请企业成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
body = gitee.Body61() # Body61 |  (optional)

try:
    # 添加或邀请企业成员
    api_instance.post_v5_enterprises_enterprise_members(enterprise, body=body)
except ApiException as e:
    print("Exception when calling EnterprisesApi->post_v5_enterprises_enterprise_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **body** | [**Body61**](Body61.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_enterprises_enterprise_week_report**
> WeekReport post_v5_enterprises_enterprise_week_report(body, enterprise)

新建周报

新建周报

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
body = gitee.Body64() # Body64 | 
enterprise = 'enterprise_example' # str | 企业的路径(path/login)

try:
    # 新建周报
    api_response = api_instance.post_v5_enterprises_enterprise_week_report(body, enterprise)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->post_v5_enterprises_enterprise_week_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body64**](Body64.md)|  | 
 **enterprise** | **str**| 企业的路径(path/login) | 

### Return type

[**WeekReport**](WeekReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_enterprises_enterprise_week_reports_id_comment**
> Note post_v5_enterprises_enterprise_week_reports_id_comment(body, enterprise, id)

评论周报

评论周报

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
body = gitee.Body62() # Body62 | 
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
id = 56 # int | 周报ID

try:
    # 评论周报
    api_response = api_instance.post_v5_enterprises_enterprise_week_reports_id_comment(body, enterprise, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->post_v5_enterprises_enterprise_week_reports_id_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body62**](Body62.md)|  | 
 **enterprise** | **str**| 企业的路径(path/login) | 
 **id** | **int**| 周报ID | 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_enterprises_enterprise_members_username**
> EnterpriseMember put_v5_enterprises_enterprise_members_username(enterprise, username, body=body)

修改企业成员权限或备注

修改企业成员权限或备注

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.EnterprisesApi()
enterprise = 'enterprise_example' # str | 企业的路径(path/login)
username = 'username_example' # str | 用户名(username/login)
body = gitee.Body66() # Body66 |  (optional)

try:
    # 修改企业成员权限或备注
    api_response = api_instance.put_v5_enterprises_enterprise_members_username(enterprise, username, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnterprisesApi->put_v5_enterprises_enterprise_members_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| 企业的路径(path/login) | 
 **username** | **str**| 用户名(username/login) | 
 **body** | [**Body66**](Body66.md)|  | [optional] 

### Return type

[**EnterpriseMember**](EnterpriseMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

