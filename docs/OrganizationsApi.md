# gitee.OrganizationsApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_orgs_org_memberships_username**](OrganizationsApi.md#delete_v5_orgs_org_memberships_username) | **DELETE** /v5/orgs/{org}/memberships/{username} | 移除授权用户所管理组织中的成员
[**delete_v5_user_memberships_orgs_org**](OrganizationsApi.md#delete_v5_user_memberships_orgs_org) | **DELETE** /v5/user/memberships/orgs/{org} | 退出一个组织
[**get_v5_orgs_org**](OrganizationsApi.md#get_v5_orgs_org) | **GET** /v5/orgs/{org} | 获取一个组织
[**get_v5_orgs_org_followers**](OrganizationsApi.md#get_v5_orgs_org_followers) | **GET** /v5/orgs/{org}/followers | 列出指定组织的所有关注者
[**get_v5_orgs_org_members**](OrganizationsApi.md#get_v5_orgs_org_members) | **GET** /v5/orgs/{org}/members | 列出一个组织的所有成员
[**get_v5_orgs_org_memberships_username**](OrganizationsApi.md#get_v5_orgs_org_memberships_username) | **GET** /v5/orgs/{org}/memberships/{username} | 获取授权用户所属组织的一个成员
[**get_v5_user_memberships_orgs**](OrganizationsApi.md#get_v5_user_memberships_orgs) | **GET** /v5/user/memberships/orgs | 列出授权用户在所属组织的成员资料
[**get_v5_user_memberships_orgs_org**](OrganizationsApi.md#get_v5_user_memberships_orgs_org) | **GET** /v5/user/memberships/orgs/{org} | 获取授权用户在一个组织的成员资料
[**get_v5_user_orgs**](OrganizationsApi.md#get_v5_user_orgs) | **GET** /v5/user/orgs | 列出授权用户所属的组织
[**get_v5_users_username_orgs**](OrganizationsApi.md#get_v5_users_username_orgs) | **GET** /v5/users/{username}/orgs | 列出用户所属的组织
[**patch_v5_orgs_org**](OrganizationsApi.md#patch_v5_orgs_org) | **PATCH** /v5/orgs/{org} | 更新授权用户所管理的组织资料
[**patch_v5_user_memberships_orgs_org**](OrganizationsApi.md#patch_v5_user_memberships_orgs_org) | **PATCH** /v5/user/memberships/orgs/{org} | 更新授权用户在一个组织的成员资料
[**post_v5_users_organization**](OrganizationsApi.md#post_v5_users_organization) | **POST** /v5/users/organization | 创建组织
[**put_v5_orgs_org_memberships_username**](OrganizationsApi.md#put_v5_orgs_org_memberships_username) | **PUT** /v5/orgs/{org}/memberships/{username} | 增加或更新授权用户所管理组织的成员

# **delete_v5_orgs_org_memberships_username**
> delete_v5_orgs_org_memberships_username(org, username, access_token=access_token)

移除授权用户所管理组织中的成员

移除授权用户所管理组织中的成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
org = 'org_example' # str | 组织的路径(path/login)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 移除授权用户所管理组织中的成员
    api_instance.delete_v5_orgs_org_memberships_username(org, username, access_token=access_token)
except ApiException as e:
    print("Exception when calling OrganizationsApi->delete_v5_orgs_org_memberships_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
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

# **delete_v5_user_memberships_orgs_org**
> delete_v5_user_memberships_orgs_org(org, access_token=access_token)

退出一个组织

退出一个组织

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 退出一个组织
    api_instance.delete_v5_user_memberships_orgs_org(org, access_token=access_token)
except ApiException as e:
    print("Exception when calling OrganizationsApi->delete_v5_user_memberships_orgs_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_orgs_org**
> Group get_v5_orgs_org(org, access_token=access_token)

获取一个组织

获取一个组织

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一个组织
    api_response = api_instance.get_v5_orgs_org(org, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_v5_orgs_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_orgs_org_followers**
> list[GroupFollowers] get_v5_orgs_org_followers(org, access_token=access_token, page=page, per_page=per_page)

列出指定组织的所有关注者

列出指定组织的所有关注者

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出指定组织的所有关注者
    api_response = api_instance.get_v5_orgs_org_followers(org, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_v5_orgs_org_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[GroupFollowers]**](GroupFollowers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_orgs_org_members**
> list[UserBasic] get_v5_orgs_org_members(org, access_token=access_token, page=page, per_page=per_page, role=role)

列出一个组织的所有成员

列出一个组织的所有成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
role = 'all' # str | 根据角色筛选成员 (optional) (default to all)

try:
    # 列出一个组织的所有成员
    api_response = api_instance.get_v5_orgs_org_members(org, access_token=access_token, page=page, per_page=per_page, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_v5_orgs_org_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **role** | **str**| 根据角色筛选成员 | [optional] [default to all]

### Return type

[**list[UserBasic]**](UserBasic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_orgs_org_memberships_username**
> GroupMember get_v5_orgs_org_memberships_username(org, username, access_token=access_token)

获取授权用户所属组织的一个成员

获取授权用户所属组织的一个成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
org = 'org_example' # str | 组织的路径(path/login)
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取授权用户所属组织的一个成员
    api_response = api_instance.get_v5_orgs_org_memberships_username(org, username, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_v5_orgs_org_memberships_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_memberships_orgs**
> list[GroupMember] get_v5_user_memberships_orgs(access_token=access_token, active=active, page=page, per_page=per_page)

列出授权用户在所属组织的成员资料

列出授权用户在所属组织的成员资料

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
active = true # bool | 根据成员是否已激活进行筛选资料，缺省返回所有资料 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户在所属组织的成员资料
    api_response = api_instance.get_v5_user_memberships_orgs(access_token=access_token, active=active, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_v5_user_memberships_orgs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **active** | **bool**| 根据成员是否已激活进行筛选资料，缺省返回所有资料 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[GroupMember]**](GroupMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_memberships_orgs_org**
> GroupMember get_v5_user_memberships_orgs_org(org, access_token=access_token)

获取授权用户在一个组织的成员资料

获取授权用户在一个组织的成员资料

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取授权用户在一个组织的成员资料
    api_response = api_instance.get_v5_user_memberships_orgs_org(org, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_v5_user_memberships_orgs_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_orgs**
> list[Group] get_v5_user_orgs(access_token=access_token, page=page, per_page=per_page, admin=admin)

列出授权用户所属的组织

列出授权用户所属的组织

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
admin = true # bool | 只列出授权用户管理的组织 (optional)

try:
    # 列出授权用户所属的组织
    api_response = api_instance.get_v5_user_orgs(access_token=access_token, page=page, per_page=per_page, admin=admin)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_v5_user_orgs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **admin** | **bool**| 只列出授权用户管理的组织 | [optional] 

### Return type

[**list[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_orgs**
> list[Group] get_v5_users_username_orgs(username, access_token=access_token, page=page, per_page=per_page)

列出用户所属的组织

列出用户所属的组织

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出用户所属的组织
    api_response = api_instance.get_v5_users_username_orgs(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_v5_users_username_orgs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Group]**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_orgs_org**
> GroupDetail patch_v5_orgs_org(org, access_token=access_token, email=email, location=location, name=name, description=description, html_url=html_url)

更新授权用户所管理的组织资料

更新授权用户所管理的组织资料

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str |  (optional)
email = 'email_example' # str |  (optional)
location = 'location_example' # str |  (optional)
name = 'name_example' # str |  (optional)
description = 'description_example' # str |  (optional)
html_url = 'html_url_example' # str |  (optional)

try:
    # 更新授权用户所管理的组织资料
    api_response = api_instance.patch_v5_orgs_org(org, access_token=access_token, email=email, location=location, name=name, description=description, html_url=html_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->patch_v5_orgs_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**|  | [optional] 
 **email** | **str**|  | [optional] 
 **location** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **html_url** | **str**|  | [optional] 

### Return type

[**GroupDetail**](GroupDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_user_memberships_orgs_org**
> GroupMember patch_v5_user_memberships_orgs_org(org, access_token=access_token, remark=remark)

更新授权用户在一个组织的成员资料

更新授权用户在一个组织的成员资料

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str |  (optional)
remark = 'remark_example' # str |  (optional)

try:
    # 更新授权用户在一个组织的成员资料
    api_response = api_instance.patch_v5_user_memberships_orgs_org(org, access_token=access_token, remark=remark)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->patch_v5_user_memberships_orgs_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**|  | [optional] 
 **remark** | **str**|  | [optional] 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_users_organization**
> Group post_v5_users_organization(body)

创建组织

创建组织

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
body = gitee.Body57() # Body57 | 

try:
    # 创建组织
    api_response = api_instance.post_v5_users_organization(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->post_v5_users_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body57**](Body57.md)|  | 

### Return type

[**Group**](Group.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_orgs_org_memberships_username**
> GroupMember put_v5_orgs_org_memberships_username(org, username, body=body)

增加或更新授权用户所管理组织的成员

增加或更新授权用户所管理组织的成员

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.OrganizationsApi()
org = 'org_example' # str | 组织的路径(path/login)
username = 'username_example' # str | 用户名(username/login)
body = gitee.Body60() # Body60 |  (optional)

try:
    # 增加或更新授权用户所管理组织的成员
    api_response = api_instance.put_v5_orgs_org_memberships_username(org, username, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->put_v5_orgs_org_memberships_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **username** | **str**| 用户名(username/login) | 
 **body** | [**Body60**](Body60.md)|  | [optional] 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

