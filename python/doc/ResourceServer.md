# ResourceServer

## Description

The definition for a single resource server which provides content for the gateway.


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path at which the resource server will be made available. This entry is required if the virtual\_host entry has not been specified. It is not valid to have both path and virtual\_host entries specified. | [optional] 
**virtual\_host** | **str** | The virtual host, as defined by the host header in the request, at which the resource server will be made available. Port information may also be specified if the virtual host is on a non-default port for the intended protocol. This entry is required if the path entry has not been specified. It is not valid to have both path and virtual\_host entries specified. | [optional] 
**connection\_type** | **str** | The connection type the reverse proxy will make for this resource server. | [optional] [default to 'tcp']
**transparent\_path** | **bool** | A boolean flag indicating whether or not this resource server uses a transparent path. For path type resource servers, setting this entry to true will result in the passing of the entire URL as observed by the reverse proxy to the resource server, including the value given in \"path\". If set to false the reverse proxy will filter the path from the URL and pass only the remainder of the URL to the resource server. | [optional] [default to False]
**stateful** | **bool** | A boolean flag indicating whether or not user requests, for the lifetime of a session, are always processed by the same resource server.  | [optional] [default to False]
**http2** | [**ResourceServerHttp2**](ResourceServerHttp2.md) |  | [optional] 
**identity\_headers** | [**ResourceServerIdentityHeaders**](ResourceServerIdentityHeaders.md) |  | [optional] 
**cookies** | [**ResourceServerCookies**](ResourceServerCookies.md) |  | [optional] 
**mutual\_auth** | [**ResourceServerMutualAuth**](ResourceServerMutualAuth.md) |  | [optional] 
**servers** | [**list[ResourceServerServers]**](ResourceServerServers.md) | Specifies the location of the resource server that is being protected.| [optional] 
**forms\_login** | [**list[ResourceServerFormsLogin]**](ResourceServerFormsLogin.md) | Specifies the configuration information used for performing form-based single sign-on to the protected application.| [optional] 
**health** | [**ResourceServerHealth**](ResourceServerHealth.md) |  | [optional] 
**worker\_threads** | [**ResourceServerWorkerThreads**](ResourceServerWorkerThreads.md) |  | [optional] 
**persistent\_connections** | [**ResourceServerPersistentConnections**](ResourceServerPersistentConnections.md) |  | [optional] 
**identity** | [**ResourceServerIdentity**](ResourceServerIdentity.md) |  | [optional] 

[[Back to README]](../README.md)



