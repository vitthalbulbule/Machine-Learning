# 🐍 Anaconda Installation & Virtual Environment Setup Guide

## 📌 Overview
This guide will help you:
- Install Anaconda on your system
- Create and manage virtual environments
- Run Python/Data Science projects in an isolated setup

---

## ❓ Why Use Virtual Environments?

Virtual environments are important because:
- ✅ They isolate project dependencies
- ✅ Avoid version conflicts between libraries
- ✅ Keep your system clean
- ✅ Make projects reproducible and professional

---

## ⚙️ Step 1: Download Anaconda

1. Visit: https://www.anaconda.com/download  
2. Select your OS:
   - Windows
   - macOS
   - Linux  
3. Download the latest Python 3 version

---

## ⚙️ Step 2: Install Anaconda

### 🪟 Windows
1. Run `.exe` installer  
2. Click **Next → I Agree**  
3. Choose **Just Me (Recommended)**  
4. Select installation path  
5. (Optional) ✔️ Add Anaconda to PATH  
6. Click **Install → Finish**

---

🌱 Step 5: Create Virtual Environment
conda create --name myenv python=3.10

▶️ Step 6: Activate Environment
conda activate myenv

⏹️ Step 7: Deactivate Environment
conda deactivate

📦 Step 8: Install Packages

Using conda:
conda install numpy pandas matplotlib

Using pip:
pip install scikit-learn

📋 Step 9: List All Environments
conda env list

❌ Step 10: Delete Environment
conda remove --name myenv --all
