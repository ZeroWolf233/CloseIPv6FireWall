import paramiko


def run_commands():
    # 定义 SSH 连接信息
    hostname = '192.168.31.1'
    username = 'root'
    password = 'root'
    port = 22

    # 定义要执行的命令
    commands = [
        'ip6tables -F',
        'ip6tables -X',
        'ip6tables -P INPUT ACCEPT',
        'ip6tables -P OUTPUT ACCEPT',
        'ip6tables -P FORWARD ACCEPT'
    ]

    # 创建 SSH 客户端
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 连接到服务器
        ssh.connect(hostname, port, username, password)

        # 执行每个命令
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            print(f"执行命令: {command}")
            print(stdout.read().decode())
            print(stderr.read().decode())

    except Exception as e:
        print(f"连接或执行命令失败: {e}")

    finally:
        ssh.close()


if __name__ == '__main__':
    run_commands()
