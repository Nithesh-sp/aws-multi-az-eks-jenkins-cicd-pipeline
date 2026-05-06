resource "aws_ecr_repository" "app_repo" {
  name = "django-app"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name = "django-app-repo"
  }
}
