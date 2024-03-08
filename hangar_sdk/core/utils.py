import asyncio
import subprocess
import time


def execute_command(command, file=None, env=None, store_func=None, path=None):
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        env=env,
        cwd=path,
    )

    # Read and print the output line by line
    for line in process.stdout:
        print(line, end="")  # Print without adding an extra newline
        if file:
            print(line, end="", file=file, flush=True)
        if store_func:
            store_func(line)

    # Wait for the command to complete
    process.wait()
    print("\nEND")

    # Return the exit code and the output
    return process.returncode, process.stdout, process.stderr


async def aexecute_command(
    command, file=None, env=None, store_func=None, store_funcs=[], path=None
):
    # Create a subprocess using asyncio
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
        env=env,
        cwd=path,
    )

    # Async read and manually decode the output line by line
    async for line in process.stdout:
        decoded_line = line.decode("utf-8")  # Manually decode the line
        print(decoded_line, end="")
        if file:
            print(decoded_line, end="", file=file, flush=True)
        if store_func:
            # print(store_func)
            await store_func(decoded_line, int(time.time() * 1000))

        if len(store_funcs) > 0:
            for store_func in store_funcs:
                await store_func(decoded_line, int(time.time() * 1000))

    # Wait for the command to complete
    await process.wait()
    print("\nEND")

    # Return the exit code
    return process.returncode, process.stdout, process.stderr
