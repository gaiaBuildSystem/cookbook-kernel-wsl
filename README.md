# Cookbook Kernel WSL 2

Welcome to the Cookbook Kernel WSL 2 project! This README provides an overview of the project, setup instructions, and usage guidelines.

## Table of Contents

- [Introduction](#introduction)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Cookbook Kernel WSL 2 has recipes to build and generate custom Linux kernels for Windows Subsystem for Linux 2 (WSL 2) using Gaia project.

## Configuration

To get started with Cookbook Kernel WSL, follow these steps:

1. Clone the Gaia core repository:

    ```sh
    git clone https://github.com/gaiaBuildSystem/gaia.git
    ```

2. Clone the Cookbook Kernel WSL repository:

    ```sh
    git clone https://github.com/gaiaBuildSystem/cookbook-kernel-wsl.git
    ```

3. Navigate to the Gaia folder and run the dependency script:

    ```sh
    cd gaia
    ./scripts/deps
    ```

With this you should have all the dependencies installed and ready to build the kernel.

## Usage

1. To build the kernel navigate to the root folder where you clone the Gaia repo and the Cookbook Kernel WSL repo and run the following command:

    ```sh
    ./gaia/scripts/bitcook/gaia.ts \
        --buildPath /home/$USER/workdir \
        --distro ./cookbook-kernel-wsl/distro-kernel-x86-wsl2.json
    ```

In the end of the build process you should have a kernel image ready to be used with WSL 2. The `bzImage` file should be located at `./build-microhobby-x86-wsl2/tmp/wsl-amd64/deploy/bzImage`.

## Contributing

We welcome contributions! For now only `x86-64` builds are supported.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
