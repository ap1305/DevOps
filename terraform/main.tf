resource "aws_instance" "Server1" {
  ami                    = "ami-0f918f7e67a3323f0"
  instance_type          = "t2.micro"
  key_name               = aws_key_pair.web.id
  vpc_security_group_ids = [aws_security_group.ssh-access.id]
}



resource "aws_key_pair" "web" {
  public_key = file("/home/jenkins/.ssh/id_rsa.pub")
}

resource "aws_security_group" "ssh-access" {
  name = "ssh-access"
  dynamic "ingress" {
    for_each = var.ingress_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}

output "public_ip" {
  value = aws_instance.Server1.public_ip
}

resource "null_resource" "command" {
  provisioner "local-exec" {
    command = "echo '${aws_instance.Server1.public_ip} ansible_user=ubuntu ansible_ssh_private_key_file=/home/jenkins/.ssh/id_rsa' >/home/jenkins/ansible/inventory.ini"
  }
}
