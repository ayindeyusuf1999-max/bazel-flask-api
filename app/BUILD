load("@rules_python//python:defs.bzl", "py_library", "py_binary")

py_library(
    name = "main_lib",
    srcs = ["main.py"],
    visibility = ["//visibility:public"],
)

py_binary(
    name = "server",
    srcs = ["main.py"],
    main = "main.py",
    deps = [],
)