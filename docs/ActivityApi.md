# gitee.ActivityApi

All URIs are relative to *//https://gitee.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v5_user_starred_owner_repo**](ActivityApi.md#delete_v5_user_starred_owner_repo) | **DELETE** /v5/user/starred/{owner}/{repo} | 取消 star 一个仓库
[**delete_v5_user_subscriptions_owner_repo**](ActivityApi.md#delete_v5_user_subscriptions_owner_repo) | **DELETE** /v5/user/subscriptions/{owner}/{repo} | 取消 watch 一个仓库
[**get_v5_networks_owner_repo_events**](ActivityApi.md#get_v5_networks_owner_repo_events) | **GET** /v5/networks/{owner}/{repo}/events | 列出仓库的所有公开动态
[**get_v5_notifications_count**](ActivityApi.md#get_v5_notifications_count) | **GET** /v5/notifications/count | 获取授权用户的通知数
[**get_v5_notifications_messages**](ActivityApi.md#get_v5_notifications_messages) | **GET** /v5/notifications/messages | 列出授权用户的所有私信
[**get_v5_notifications_messages_id**](ActivityApi.md#get_v5_notifications_messages_id) | **GET** /v5/notifications/messages/{id} | 获取一条私信
[**get_v5_notifications_threads**](ActivityApi.md#get_v5_notifications_threads) | **GET** /v5/notifications/threads | 列出授权用户的所有通知
[**get_v5_notifications_threads_id**](ActivityApi.md#get_v5_notifications_threads_id) | **GET** /v5/notifications/threads/{id} | 获取一条通知
[**get_v5_orgs_org_events**](ActivityApi.md#get_v5_orgs_org_events) | **GET** /v5/orgs/{org}/events | 列出组织的公开动态
[**get_v5_repos_owner_repo_events**](ActivityApi.md#get_v5_repos_owner_repo_events) | **GET** /v5/repos/{owner}/{repo}/events | 列出仓库的所有动态
[**get_v5_repos_owner_repo_notifications**](ActivityApi.md#get_v5_repos_owner_repo_notifications) | **GET** /v5/repos/{owner}/{repo}/notifications | 列出一个仓库里的通知
[**get_v5_repos_owner_repo_stargazers**](ActivityApi.md#get_v5_repos_owner_repo_stargazers) | **GET** /v5/repos/{owner}/{repo}/stargazers | 列出 star 了仓库的用户
[**get_v5_repos_owner_repo_subscribers**](ActivityApi.md#get_v5_repos_owner_repo_subscribers) | **GET** /v5/repos/{owner}/{repo}/subscribers | 列出 watch 了仓库的用户
[**get_v5_user_starred**](ActivityApi.md#get_v5_user_starred) | **GET** /v5/user/starred | 列出授权用户 star 了的仓库
[**get_v5_user_starred_owner_repo**](ActivityApi.md#get_v5_user_starred_owner_repo) | **GET** /v5/user/starred/{owner}/{repo} | 检查授权用户是否 star 了一个仓库
[**get_v5_user_subscriptions**](ActivityApi.md#get_v5_user_subscriptions) | **GET** /v5/user/subscriptions | 列出授权用户 watch 了的仓库
[**get_v5_user_subscriptions_owner_repo**](ActivityApi.md#get_v5_user_subscriptions_owner_repo) | **GET** /v5/user/subscriptions/{owner}/{repo} | 检查授权用户是否 watch 了一个仓库
[**get_v5_users_username_events**](ActivityApi.md#get_v5_users_username_events) | **GET** /v5/users/{username}/events | 列出用户的动态
[**get_v5_users_username_events_orgs_org**](ActivityApi.md#get_v5_users_username_events_orgs_org) | **GET** /v5/users/{username}/events/orgs/{org} | 列出用户所属组织的动态
[**get_v5_users_username_events_public**](ActivityApi.md#get_v5_users_username_events_public) | **GET** /v5/users/{username}/events/public | 列出用户的公开动态
[**get_v5_users_username_received_events**](ActivityApi.md#get_v5_users_username_received_events) | **GET** /v5/users/{username}/received_events | 列出一个用户收到的动态
[**get_v5_users_username_received_events_public**](ActivityApi.md#get_v5_users_username_received_events_public) | **GET** /v5/users/{username}/received_events/public | 列出一个用户收到的公开动态
[**get_v5_users_username_starred**](ActivityApi.md#get_v5_users_username_starred) | **GET** /v5/users/{username}/starred | 列出用户 star 了的仓库
[**get_v5_users_username_subscriptions**](ActivityApi.md#get_v5_users_username_subscriptions) | **GET** /v5/users/{username}/subscriptions | 列出用户 watch 了的仓库
[**patch_v5_notifications_messages_id**](ActivityApi.md#patch_v5_notifications_messages_id) | **PATCH** /v5/notifications/messages/{id} | 标记一条私信为已读
[**patch_v5_notifications_threads_id**](ActivityApi.md#patch_v5_notifications_threads_id) | **PATCH** /v5/notifications/threads/{id} | 标记一条通知为已读
[**post_v5_notifications_messages**](ActivityApi.md#post_v5_notifications_messages) | **POST** /v5/notifications/messages | 发送私信给指定用户
[**put_v5_notifications_messages**](ActivityApi.md#put_v5_notifications_messages) | **PUT** /v5/notifications/messages | 标记所有私信为已读
[**put_v5_notifications_threads**](ActivityApi.md#put_v5_notifications_threads) | **PUT** /v5/notifications/threads | 标记所有通知为已读
[**put_v5_repos_owner_repo_notifications**](ActivityApi.md#put_v5_repos_owner_repo_notifications) | **PUT** /v5/repos/{owner}/{repo}/notifications | 标记一个仓库里的通知为已读
[**put_v5_user_starred_owner_repo**](ActivityApi.md#put_v5_user_starred_owner_repo) | **PUT** /v5/user/starred/{owner}/{repo} | star 一个仓库
[**put_v5_user_subscriptions_owner_repo**](ActivityApi.md#put_v5_user_subscriptions_owner_repo) | **PUT** /v5/user/subscriptions/{owner}/{repo} | watch 一个仓库

# **delete_v5_user_starred_owner_repo**
> delete_v5_user_starred_owner_repo(owner, repo, access_token=access_token)

取消 star 一个仓库

取消 star 一个仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消 star 一个仓库
    api_instance.delete_v5_user_starred_owner_repo(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->delete_v5_user_starred_owner_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v5_user_subscriptions_owner_repo**
> delete_v5_user_subscriptions_owner_repo(owner, repo, access_token=access_token)

取消 watch 一个仓库

取消 watch 一个仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 取消 watch 一个仓库
    api_instance.delete_v5_user_subscriptions_owner_repo(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->delete_v5_user_subscriptions_owner_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_networks_owner_repo_events**
> list[Event] get_v5_networks_owner_repo_events(owner, repo, access_token=access_token, page=page, per_page=per_page)

列出仓库的所有公开动态

列出仓库的所有公开动态

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出仓库的所有公开动态
    api_response = api_instance.get_v5_networks_owner_repo_events(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_networks_owner_repo_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_notifications_count**
> UserNotificationCount get_v5_notifications_count(access_token=access_token, unread=unread)

获取授权用户的通知数

获取授权用户的通知数

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只获取未读消息，默认：否 (optional)

try:
    # 获取授权用户的通知数
    api_response = api_instance.get_v5_notifications_count(access_token=access_token, unread=unread)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_notifications_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **unread** | **bool**| 是否只获取未读消息，默认：否 | [optional] 

### Return type

[**UserNotificationCount**](UserNotificationCount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_notifications_messages**
> list[UserMessageList] get_v5_notifications_messages(access_token=access_token, unread=unread, since=since, before=before, ids=ids, page=page, per_page=per_page)

列出授权用户的所有私信

列出授权用户的所有私信

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只显示未读私信，默认：否 (optional)
since = 'since_example' # str | 只获取在给定时间后更新的私信，要求时间格式为 ISO 8601 (optional)
before = 'before_example' # str | 只获取在给定时间前更新的私信，要求时间格式为 ISO 8601 (optional)
ids = 'ids_example' # str | 指定一组私信 ID，以 , 分隔 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户的所有私信
    api_response = api_instance.get_v5_notifications_messages(access_token=access_token, unread=unread, since=since, before=before, ids=ids, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_notifications_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **unread** | **bool**| 是否只显示未读私信，默认：否 | [optional] 
 **since** | **str**| 只获取在给定时间后更新的私信，要求时间格式为 ISO 8601 | [optional] 
 **before** | **str**| 只获取在给定时间前更新的私信，要求时间格式为 ISO 8601 | [optional] 
 **ids** | **str**| 指定一组私信 ID，以 , 分隔 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[UserMessageList]**](UserMessageList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_notifications_messages_id**
> UserMessage get_v5_notifications_messages_id(id, access_token=access_token)

获取一条私信

获取一条私信

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
id = 'id_example' # str | 私信的 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一条私信
    api_response = api_instance.get_v5_notifications_messages_id(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_notifications_messages_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 私信的 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**UserMessage**](UserMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_notifications_threads**
> list[UserNotificationList] get_v5_notifications_threads(access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)

列出授权用户的所有通知

列出授权用户的所有通知

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只获取未读消息，默认：否 (optional)
participating = true # bool | 是否只获取自己直接参与的消息，默认：否 (optional)
type = 'all' # str | 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知 (optional) (default to all)
since = 'since_example' # str | 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601 (optional)
before = 'before_example' # str | 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601 (optional)
ids = 'ids_example' # str | 指定一组通知 ID，以 , 分隔 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户的所有通知
    api_response = api_instance.get_v5_notifications_threads(access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_notifications_threads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **unread** | **bool**| 是否只获取未读消息，默认：否 | [optional] 
 **participating** | **bool**| 是否只获取自己直接参与的消息，默认：否 | [optional] 
 **type** | **str**| 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知 | [optional] [default to all]
 **since** | **str**| 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601 | [optional] 
 **before** | **str**| 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601 | [optional] 
 **ids** | **str**| 指定一组通知 ID，以 , 分隔 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[UserNotificationList]**](UserNotificationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_notifications_threads_id**
> UserNotification get_v5_notifications_threads_id(id, access_token=access_token)

获取一条通知

获取一条通知

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
id = 'id_example' # str | 通知的 ID
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 获取一条通知
    api_response = api_instance.get_v5_notifications_threads_id(id, access_token=access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_notifications_threads_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 通知的 ID | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

[**UserNotification**](UserNotification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_orgs_org_events**
> list[Event] get_v5_orgs_org_events(org, access_token=access_token, page=page, per_page=per_page)

列出组织的公开动态

列出组织的公开动态

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出组织的公开动态
    api_response = api_instance.get_v5_orgs_org_events(org, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_orgs_org_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_events**
> list[Event] get_v5_repos_owner_repo_events(owner, repo, access_token=access_token, page=page, per_page=per_page)

列出仓库的所有动态

列出仓库的所有动态

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出仓库的所有动态
    api_response = api_instance.get_v5_repos_owner_repo_events(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_repos_owner_repo_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_notifications**
> list[UserNotificationList] get_v5_repos_owner_repo_notifications(owner, repo, access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)

列出一个仓库里的通知

列出一个仓库里的通知

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
unread = true # bool | 是否只获取未读消息，默认：否 (optional)
participating = true # bool | 是否只获取自己直接参与的消息，默认：否 (optional)
type = 'all' # str | 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知 (optional) (default to all)
since = 'since_example' # str | 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601 (optional)
before = 'before_example' # str | 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601 (optional)
ids = 'ids_example' # str | 指定一组通知 ID，以 , 分隔 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出一个仓库里的通知
    api_response = api_instance.get_v5_repos_owner_repo_notifications(owner, repo, access_token=access_token, unread=unread, participating=participating, type=type, since=since, before=before, ids=ids, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_repos_owner_repo_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **unread** | **bool**| 是否只获取未读消息，默认：否 | [optional] 
 **participating** | **bool**| 是否只获取自己直接参与的消息，默认：否 | [optional] 
 **type** | **str**| 筛选指定类型的通知，all：所有，event：事件通知，referer：@ 通知 | [optional] [default to all]
 **since** | **str**| 只获取在给定时间后更新的消息，要求时间格式为 ISO 8601 | [optional] 
 **before** | **str**| 只获取在给定时间前更新的消息，要求时间格式为 ISO 8601 | [optional] 
 **ids** | **str**| 指定一组通知 ID，以 , 分隔 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[UserNotificationList]**](UserNotificationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_stargazers**
> list[ProjectStargazers] get_v5_repos_owner_repo_stargazers(owner, repo, access_token=access_token, page=page, per_page=per_page)

列出 star 了仓库的用户

列出 star 了仓库的用户

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出 star 了仓库的用户
    api_response = api_instance.get_v5_repos_owner_repo_stargazers(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_repos_owner_repo_stargazers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[ProjectStargazers]**](ProjectStargazers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_repos_owner_repo_subscribers**
> list[ProjectWatchers] get_v5_repos_owner_repo_subscribers(owner, repo, access_token=access_token, page=page, per_page=per_page)

列出 watch 了仓库的用户

列出 watch 了仓库的用户

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出 watch 了仓库的用户
    api_response = api_instance.get_v5_repos_owner_repo_subscribers(owner, repo, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_repos_owner_repo_subscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[ProjectWatchers]**](ProjectWatchers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_starred**
> list[Project] get_v5_user_starred(access_token=access_token, sort=sort, direction=direction, page=page, per_page=per_page)

列出授权用户 star 了的仓库

列出授权用户 star 了的仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'created' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional) (default to created)
direction = 'desc' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional) (default to desc)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户 star 了的仓库
    api_response = api_instance.get_v5_user_starred(access_token=access_token, sort=sort, direction=direction, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_user_starred: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **sort** | **str**| 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 | [optional] [default to created]
 **direction** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] [default to desc]
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_starred_owner_repo**
> get_v5_user_starred_owner_repo(owner, repo, access_token=access_token)

检查授权用户是否 star 了一个仓库

检查授权用户是否 star 了一个仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 检查授权用户是否 star 了一个仓库
    api_instance.get_v5_user_starred_owner_repo(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_user_starred_owner_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_subscriptions**
> list[Project] get_v5_user_subscriptions(access_token=access_token, sort=sort, direction=direction, page=page, per_page=per_page)

列出授权用户 watch 了的仓库

列出授权用户 watch 了的仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
access_token = 'access_token_example' # str | 用户授权码 (optional)
sort = 'created' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional) (default to created)
direction = 'desc' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional) (default to desc)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出授权用户 watch 了的仓库
    api_response = api_instance.get_v5_user_subscriptions(access_token=access_token, sort=sort, direction=direction, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_user_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token** | **str**| 用户授权码 | [optional] 
 **sort** | **str**| 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 | [optional] [default to created]
 **direction** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] [default to desc]
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_user_subscriptions_owner_repo**
> get_v5_user_subscriptions_owner_repo(owner, repo, access_token=access_token)

检查授权用户是否 watch 了一个仓库

检查授权用户是否 watch 了一个仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
access_token = 'access_token_example' # str | 用户授权码 (optional)

try:
    # 检查授权用户是否 watch 了一个仓库
    api_instance.get_v5_user_subscriptions_owner_repo(owner, repo, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_user_subscriptions_owner_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **access_token** | **str**| 用户授权码 | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_events**
> list[Event] get_v5_users_username_events(username, access_token=access_token, page=page, per_page=per_page)

列出用户的动态

列出用户的动态

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出用户的动态
    api_response = api_instance.get_v5_users_username_events(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_events_orgs_org**
> list[Event] get_v5_users_username_events_orgs_org(username, org, access_token=access_token, page=page, per_page=per_page)

列出用户所属组织的动态

列出用户所属组织的动态

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
username = 'username_example' # str | 用户名(username/login)
org = 'org_example' # str | 组织的路径(path/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出用户所属组织的动态
    api_response = api_instance.get_v5_users_username_events_orgs_org(username, org, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_events_orgs_org: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **org** | **str**| 组织的路径(path/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_events_public**
> list[Event] get_v5_users_username_events_public(username, access_token=access_token, page=page, per_page=per_page)

列出用户的公开动态

列出用户的公开动态

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出用户的公开动态
    api_response = api_instance.get_v5_users_username_events_public(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_events_public: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_received_events**
> list[Event] get_v5_users_username_received_events(username, access_token=access_token, page=page, per_page=per_page)

列出一个用户收到的动态

列出一个用户收到的动态

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出一个用户收到的动态
    api_response = api_instance.get_v5_users_username_received_events(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_received_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_received_events_public**
> list[Event] get_v5_users_username_received_events_public(username, access_token=access_token, page=page, per_page=per_page)

列出一个用户收到的公开动态

列出一个用户收到的公开动态

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)

try:
    # 列出一个用户收到的公开动态
    api_response = api_instance.get_v5_users_username_received_events_public(username, access_token=access_token, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_received_events_public: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]

### Return type

[**list[Event]**](Event.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_starred**
> list[Project] get_v5_users_username_starred(username, access_token=access_token, page=page, per_page=per_page, sort=sort, direction=direction)

列出用户 star 了的仓库

列出用户 star 了的仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
sort = 'created' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional) (default to created)
direction = 'desc' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional) (default to desc)

try:
    # 列出用户 star 了的仓库
    api_response = api_instance.get_v5_users_username_starred(username, access_token=access_token, page=page, per_page=per_page, sort=sort, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_starred: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **sort** | **str**| 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 | [optional] [default to created]
 **direction** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] [default to desc]

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v5_users_username_subscriptions**
> list[Project] get_v5_users_username_subscriptions(username, access_token=access_token, page=page, per_page=per_page, sort=sort, direction=direction)

列出用户 watch 了的仓库

列出用户 watch 了的仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
username = 'username_example' # str | 用户名(username/login)
access_token = 'access_token_example' # str | 用户授权码 (optional)
page = 1 # int | 当前的页码 (optional) (default to 1)
per_page = 20 # int | 每页的数量，最大为 100 (optional) (default to 20)
sort = 'created' # str | 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 (optional) (default to created)
direction = 'desc' # str | 按递增(asc)或递减(desc)排序，默认：递减 (optional) (default to desc)

try:
    # 列出用户 watch 了的仓库
    api_response = api_instance.get_v5_users_username_subscriptions(username, access_token=access_token, page=page, per_page=per_page, sort=sort, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_v5_users_username_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| 用户名(username/login) | 
 **access_token** | **str**| 用户授权码 | [optional] 
 **page** | **int**| 当前的页码 | [optional] [default to 1]
 **per_page** | **int**| 每页的数量，最大为 100 | [optional] [default to 20]
 **sort** | **str**| 根据仓库创建时间(created)或最后推送时间(updated)进行排序，默认：创建时间 | [optional] [default to created]
 **direction** | **str**| 按递增(asc)或递减(desc)排序，默认：递减 | [optional] [default to desc]

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_notifications_messages_id**
> patch_v5_notifications_messages_id(id, access_token=access_token)

标记一条私信为已读

标记一条私信为已读

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
id = 'id_example' # str | 私信的 ID
access_token = 'access_token_example' # str |  (optional)

try:
    # 标记一条私信为已读
    api_instance.patch_v5_notifications_messages_id(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->patch_v5_notifications_messages_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 私信的 ID | 
 **access_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_v5_notifications_threads_id**
> patch_v5_notifications_threads_id(id, access_token=access_token)

标记一条通知为已读

标记一条通知为已读

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
id = 'id_example' # str | 通知的 ID
access_token = 'access_token_example' # str |  (optional)

try:
    # 标记一条通知为已读
    api_instance.patch_v5_notifications_threads_id(id, access_token=access_token)
except ApiException as e:
    print("Exception when calling ActivityApi->patch_v5_notifications_threads_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| 通知的 ID | 
 **access_token** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v5_notifications_messages**
> UserMessage post_v5_notifications_messages(body)

发送私信给指定用户

发送私信给指定用户

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
body = gitee.Body71() # Body71 | 

try:
    # 发送私信给指定用户
    api_response = api_instance.post_v5_notifications_messages(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->post_v5_notifications_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body71**](Body71.md)|  | 

### Return type

[**UserMessage**](UserMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_notifications_messages**
> put_v5_notifications_messages(body=body)

标记所有私信为已读

标记所有私信为已读

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
body = gitee.Body70() # Body70 |  (optional)

try:
    # 标记所有私信为已读
    api_instance.put_v5_notifications_messages(body=body)
except ApiException as e:
    print("Exception when calling ActivityApi->put_v5_notifications_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body70**](Body70.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_notifications_threads**
> put_v5_notifications_threads(body=body)

标记所有通知为已读

标记所有通知为已读

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
body = gitee.Body68() # Body68 |  (optional)

try:
    # 标记所有通知为已读
    api_instance.put_v5_notifications_threads(body=body)
except ApiException as e:
    print("Exception when calling ActivityApi->put_v5_notifications_threads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body68**](Body68.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_repos_owner_repo_notifications**
> put_v5_repos_owner_repo_notifications(owner, repo, body=body)

标记一个仓库里的通知为已读

标记一个仓库里的通知为已读

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = gitee.Body43() # Body43 |  (optional)

try:
    # 标记一个仓库里的通知为已读
    api_instance.put_v5_repos_owner_repo_notifications(owner, repo, body=body)
except ApiException as e:
    print("Exception when calling ActivityApi->put_v5_repos_owner_repo_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**Body43**](Body43.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_user_starred_owner_repo**
> put_v5_user_starred_owner_repo(owner, repo, body=body)

star 一个仓库

star 一个仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)
body = gitee.Body49() # Body49 |  (optional)

try:
    # star 一个仓库
    api_instance.put_v5_user_starred_owner_repo(owner, repo, body=body)
except ApiException as e:
    print("Exception when calling ActivityApi->put_v5_user_starred_owner_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 
 **body** | [**Body49**](Body49.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v5_user_subscriptions_owner_repo**
> put_v5_user_subscriptions_owner_repo(body, owner, repo)

watch 一个仓库

watch 一个仓库

### Example
```python
from __future__ import print_function
import time
import gitee
from gitee.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gitee.ActivityApi()
body = gitee.Body50() # Body50 | 
owner = 'owner_example' # str | 仓库所属空间地址(企业、组织或个人的地址path)
repo = 'repo_example' # str | 仓库路径(path)

try:
    # watch 一个仓库
    api_instance.put_v5_user_subscriptions_owner_repo(body, owner, repo)
except ApiException as e:
    print("Exception when calling ActivityApi->put_v5_user_subscriptions_owner_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body50**](Body50.md)|  | 
 **owner** | **str**| 仓库所属空间地址(企业、组织或个人的地址path) | 
 **repo** | **str**| 仓库路径(path) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

