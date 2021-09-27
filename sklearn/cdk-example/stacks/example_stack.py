from aws_cdk import (
    core,
    aws_lambda,
    aws_apigatewayv2,
    aws_apigatewayv2_integrations
)


class ExampleStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ml_lambda = aws_lambda.DockerImageFunction(
            self, 'ml_lambda',
            code=aws_lambda.DockerImageCode.from_image_asset('./lambda'),
            timeout=core.Duration.minutes(1)
        )

        http_api = aws_apigatewayv2.HttpApi(self, "http_api")
        http_api.add_routes(
            path='/predict',
            methods=[aws_apigatewayv2.HttpMethod.GET],
            integration=aws_apigatewayv2_integrations.LambdaProxyIntegration(
                handler=ml_lambda
            ),
        )
