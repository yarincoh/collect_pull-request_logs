output "lambda_function_name" {
  value = aws_lambda_function.pull_request_logger.function_name
}

output "api_gateway_endpoint" {
  value = "${aws_api_gateway_rest_api.api.execution_arn}/prod/webhook"
}
