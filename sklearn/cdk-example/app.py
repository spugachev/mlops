#!/usr/bin/env python3

from aws_cdk import core

from stacks.example_stack import ExampleStack


app = core.App()
ExampleStack(app, "example")

app.synth()
