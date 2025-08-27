# github codespace環境で、lawapi-v2.yamlを使ってpythonライブラリを生成する手順
## 手順
```
$ mkdir openapi-generator
$ cd openapi-generator
$ sdk install java 11.0.28-ms
$ java --version
$ wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.6.0/openapi-generator-cli-6.6.0.jar -O openapi-generator-cli.jar
$ wget https://laws.e-gov.go.jp/api/2/swagger-ui/lawapi-v2.yaml -O lawapi-v2.yaml
$ java -jar openapi-generator-cli.jar generate -i lawapi-v2.yaml -g python -o ../python/generated_client
```

## ログ
```
@katonobu ➜ /workspaces/hourei-api-v2 (main) $ mkdir openapi-generator
@katonobu ➜ /workspaces/hourei-api-v2 (main) $ cd openapi-generator
@katonobu ➜ /workspaces/hourei-api-v2/openapi-generator (main) $ sdk install java 11.0.28-ms

Downloading: java 11.0.28-ms

In progress...

###################################################################################################################################################### 100.0%

Repackaging Java 11.0.28-ms...

Done repackaging...

Installing: java 11.0.28-ms
Done installing!

Do you want java 11.0.28-ms to be set as default? (Y/n):  y

Setting java 11.0.28-ms as default.

@katonobu ➜ /workspaces/hourei-api-v2/openapi-generator (main) $ java --version
openjdk 11.0.28 2025-07-15 LTS
OpenJDK Runtime Environment Microsoft-11913455 (build 11.0.28+6-LTS)
OpenJDK 64-Bit Server VM Microsoft-11913455 (build 11.0.28+6-LTS, mixed mode, sharing)

@katonobu ➜ /workspaces/hourei-api-v2/openapi-generator (main) $ wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.6.0/openapi-generator-cli-6.6.0.jar -O openapi-generator-cli.jar
--2025-08-27 14:25:35--  https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.6.0/openapi-generator-cli-6.6.0.jar
Resolving repo1.maven.org (repo1.maven.org)... 151.101.196.209, 2a04:4e42:a::209
Connecting to repo1.maven.org (repo1.maven.org)|151.101.196.209|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27103489 (26M) [application/java-archive]
Saving to: ‘openapi-generator-cli.jar’

openapi-generator-cli.jar                        100%[=========================================================================================================>]  25.85M  10.1MB/s    in 2.6s    

2025-08-27 14:25:39 (10.1 MB/s) - ‘openapi-generator-cli.jar’ saved [27103489/27103489]

@katonobu ➜ /workspaces/hourei-api-v2/openapi-generator (main) $ wget https://laws.e-gov.go.jp/api/2/swagger-ui/lawapi-v2.yaml -O lawapi-v2.yaml
--2025-08-27 14:25:40--  https://laws.e-gov.go.jp/api/2/swagger-ui/lawapi-v2.yaml
Resolving laws.e-gov.go.jp (laws.e-gov.go.jp)... 13.35.202.68, 13.35.202.74, 13.35.202.54, ...
Connecting to laws.e-gov.go.jp (laws.e-gov.go.jp)|13.35.202.68|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 118925 (116K) [binary/octet-stream]
Saving to: ‘lawapi-v2.yaml’

lawapi-v2.yaml                                   100%[=========================================================================================================>] 116.14K  --.-KB/s    in 0.003s  

2025-08-27 14:25:41 (45.1 MB/s) - ‘lawapi-v2.yaml’ saved [118925/118925]

@katonobu ➜ /workspaces/hourei-api-v2/openapi-generator (main) $ java -jar openapi-generator-cli.jar generate -i lawapi-v2.yaml -g python -o ../python/generated_client
[main] INFO  o.o.codegen.DefaultGenerator - Generating with dryRun=false
[main] INFO  o.o.c.ignore.CodegenIgnoreProcessor - Output directory (/workspaces/hourei-api-v2/openapi-generator/../python/generated_client) does not exist, or is inaccessible. No file (.openapi-generator-ignore) will be evaluated.
[main] INFO  o.o.codegen.DefaultGenerator - OpenAPI Generator: python (client)
[main] INFO  o.o.codegen.DefaultGenerator - Generator 'python' is considered stable.
:
:
[main] INFO  o.o.codegen.TemplateManager - writing file /workspaces/hourei-api-v2/openapi-generator/../python/generated_client/.openapi-generator/FILES
################################################################################
# Thanks for using OpenAPI Generator.                                          #
# Please consider donation to help us maintain this project 🙏                 #
# https://opencollective.com/openapi_generator/donate                          #
#                                                                              #
# This generator was written by Justin Black (https://github.com/spacether)    #
# Please support his work directly via https://github.com/sponsors/spacether 🙏#
################################################################################
@katonobu ➜ /workspaces/hourei-api-v2/openapi-generator (main) $ 