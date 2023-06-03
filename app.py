import os
from os.path import join, dirname
from dotenv import load_dotenv

from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import requests

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)
SECRET_KEY = "SPARTA"

@app.route('/')
def home():
    token_receive = request.cookies.get("mytoken")
    try:
        tes = requests.get('http://127.0.0.1:5000/warga')
        result = tes.json()
        data = result['warga']
        count_rw1 = 0
        count_rw2 = 0
        count_rw3 = 0
        count_rw4 = 0
        count_rw5= 0
        count_rw6 = 0
        count_rw7 = 0
        count_rw8 = 0
        count_rw9 = 0
        count_rw10 = 0
        count_rw11= 0
        count_rw12 = 0
        for res in data : 
            rw=res['rw']
            if (rw == '1') :
                    count_rw1 = count_rw1 + 1;
            elif (rw == '2') :
                    count_rw2 = count_rw2 + 1
            elif (rw == '3' ):
                    count_rw3 = count_rw3 + 1
            elif (rw == '4' ):
                    count_rw4 = count_rw4 + 1;
            elif (rw == '5' ):
                    count_rw5 = count_rw5 + 1;
            elif (rw == '6' ):
                    count_rw6 = count_rw6 + 1;
            elif (rw == '7' ):
                    count_rw7 = count_rw7 + 1;
            elif (rw == '8' ):
                    count_rw8 = count_rw8 + 1;
            elif (rw == '9' ):
                    count_rw9 = count_rw9 + 1;
            elif (rw == '10'):
                    count_rw10 = count_rw10 + 1;
            elif (rw == '11'):
                    count_rw11 = count_rw11 + 1;
            elif (rw == '12'):
                    count_rw12 = count_rw12 + 1;
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        print("ananda",payload)
        user_info = db.akun.find_one({"username": payload["id"]})
        print("salman",user_info)
        wilayah = user_info['wilayah']
        ket_rw = user_info['username'][-1]
        return render_template("home.html", user_info=user_info,
        rw1 = count_rw1,
        rw2 = count_rw2,
        rw3 = count_rw3,
        rw4 = count_rw4,
        rw5 = count_rw5,
        rw6 = count_rw6,
        rw7 = count_rw7,
        rw8 = count_rw8,
        rw9 = count_rw9,
        rw10 = count_rw10,
        rw11 = count_rw11,
        rw12= count_rw12,
        get_rw = ket_rw,
        wilayah = wilayah)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="Your token has expired"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="There was problem logging you in"))

@app.route("/warga", methods=["GET"])
def warga_get():
    warga_list = list(db.warga.find({}, {'_id': False}))
    return jsonify({'warga': warga_list})

@app.route("/warga", methods=["POST"])
def warga_post():
    token_receive = request.cookies.get("mytoken")
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
    user_info = db.akun.find_one({"username": payload["id"]})
    ket_rw = user_info['username'][-1]
    nama_receive = request.form['nama_give']
    nik_receive = request.form['nik_give']
    ttl_receive = request.form['ttl_give']
    tLahir_receive = request.form['tLahir_give']
    jk_receive = request.form['jk_give']
    noKK_receive = request.form['noKK_give']
    kepala_receive = request.form['kepala_give']
    rt_receive = request.form['rt_give']
    agama_receive = request.form['agama_give']
    pendidikan_receive = request.form['pendidikan_give']
    jenisPekerjaan_receive = request.form['jenisPekerjaan_give']
    golDarah_receive = request.form['golDarah_give']

    doc = {
          'nama' : nama_receive,
          'nik' : nik_receive,
          'noKK' : noKK_receive,
          'tgl_lahir' : ttl_receive,
          'tmpt_lahir' : tLahir_receive,
          'jk' : jk_receive,
          'rw' : ket_rw,
          'kepala' : kepala_receive,
          'rt': rt_receive,
          'agama' : agama_receive,
          'pendidikan' : pendidikan_receive,
          'pekerjaan' : jenisPekerjaan_receive,
          'golDarah' : golDarah_receive
    }
    db.warga.insert_one(doc)
    return jsonify({'msg':'Data Disimpan!'})

@app.route("/akun", methods=["GET"])
def rw_get():
    rw = list(db.akun.find({}, {'_id': False}))
    return jsonify({'akun': rw})

@app.route("/login")
def login():
    msg = request.args.get("msg")
    tes = requests.get('http://127.0.0.1:5000/warga')
    result = tes.json()
    data = result['warga']
    count_rw1 = 0
    count_rw2 = 0
    count_rw3 = 0
    count_rw4 = 0
    count_rw5= 0
    count_rw6 = 0
    count_rw7 = 0
    count_rw8 = 0
    count_rw9 = 0
    count_rw10 = 0
    count_rw11= 0
    count_rw12 = 0
    for res in data : 
        rw=res['rw']
        if (rw == '1') :
                count_rw1 = count_rw1 + 1;
        elif (rw == '2') :
                count_rw2 = count_rw2 + 1;
        elif (rw == '3' ):
                count_rw3 = count_rw3 + 1;
        elif (rw == '4' ):
                count_rw4 = count_rw4 + 1;
        elif (rw == '5' ):
                count_rw5 = count_rw5 + 1;
        elif (rw == '6' ):
                count_rw6 = count_rw6 + 1;
        elif (rw == '7' ):
                count_rw7 = count_rw7 + 1;
        elif (rw == '8' ):
                count_rw8 = count_rw8 + 1;
        elif (rw == '9' ):
                count_rw9 = count_rw9 + 1;
        elif (rw == '10'):
                count_rw10 = count_rw10 + 1;
        elif (rw == '11'):
                count_rw11 = count_rw11 + 1;
        elif (rw == '12'):
                count_rw12 = count_rw12 + 1;
    return render_template(
        'index.html', 
        rw1 = count_rw1,
        rw2 = count_rw2,
        rw3 = count_rw3,
        rw4 = count_rw4,
        rw5 = count_rw5,
        rw6 = count_rw6,
        rw7 = count_rw7,
        rw8 = count_rw8,
        rw9 = count_rw9,
        rw10 = count_rw10,
        rw11 = count_rw11,
        rw12= count_rw12,
        msg=msg,
    ) 
    
@app.route("/sign_in", methods=["POST"])
def sign_in():
    # Sign in
    username_receive = request.form["username_give"]
    password_receive = request.form["password_give"]
    pw_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()
    print(username_receive, pw_hash)
    result = db.akun.find_one(
        {
            "username": username_receive,
            "password": pw_hash,
        }
    )
    if result:
        payload = {
            "id": username_receive,
            # the token will be valid for 24 hours
            "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256").decode("utf-8")

        return jsonify(
            {
                "result": "success",
                "token": token,
            }
        )
    # Let's also handle the case where the id and
    # password combination cannot be found
    else:
        return jsonify(
            {
                "result": "fail",
                "msg": "We could not find a user with that id/password combination",
            }
        )

# @app.route("/input")
# def input():
#     return render_template(
#            'input.html'
#     )

@app.route("/api/login", methods=["POST"])
def api_login():
    id_receive = request.form["id_give"]
    pw_receive = request.form["pw_give"]

		# Kita akan mengenkripsi passwordnya disini dengan 
    # cara yang sama seperti user pertama kali mendaftar untuk layanan web
    pw_hash = hashlib.sha256(pw_receive.encode("utf-8")).hexdigest()

		# Jika kita bisa menemukan user tersebut, kita membuat
    # Token JWT baru untuk mereka
    result = db.akun.find_one({"id": id_receive, "pw": pw_hash})

    if result is not None:
				# Untuk menghasilkan token JWT, kita perlu 
        # suatu "payload" dan "kunci rahasia"

        # "kunci rahasia" diperlukan untuk mendekripsi 
        # token dan melihat payload 

        # payload dibawah membawa id user dan tanggal expired token, 
        # artinya anda jika anda dekripsi tokennya, anda  
        # bisa tau id user 

        # jika kita mengatur "exp" tanggal expired, lalu suatu errror 
        # muncul ketika kita mencoba dekripsi tokennya menggunakan 
        # kunci rahasia ketika token telah expired. Ini merupakan hal bagus!
        payload = {
            "id": id_receive,
            "exp": datetime.utcnow() + timedelta(seconds = 60 * 60 * 24),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256").decode("utf-8")

        # mengembalikan token ke client
        return jsonify({"result": "success", "token": token})
		# Jika kita tidak bisa menemukan user di database,
    # kita bisa menangani kasus tersebut disini
    else:
        return jsonify(
            {"result": "fail", "msg": "Either your email or your password is incorrect"}
        )
        # [Endpoint API verifikasi informasi user]
        # Ini merupakan endpoint API yang hanya bisa
        # menerima request dari user terotentikasi
        # Anda hanya perlu memasukkan token yang valid
        # pada request anda untuk mendapatkan akses ke
        # Endpoint API ini. Sistem ini wajar karena
        # beberapa informasi sebaiknya private untuk setiap user
        # (contoh. shopping cart atau data akun user)

@app.route("/api/nick", methods=["GET"])
def api_valid():
    token_receive = request.cookies.get("mytoken")

		# apakah anda sudah melihat pernyataan try/catch sebelumnya?
    try:
				# kita akan coba decode tokennya dengan kunci rahasia
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
				# jika tidak ada masalah, kita seharusnya melihat
				# payload terdekripsi muncul di terminal kita!
        print(payload)

				# payload terdekripsinya seharusnya berisi id user
				# kita bisa menggunakan id ini untuk mencari data user
				# dari database dan mengembalikannya ke user
        userinfo = db.akun.find_one({"id": payload["id"]}, {"_id": 0})
        return jsonify({"result": "success", "nickname": userinfo["nick"]})
    except jwt.ExpiredSignatureError:
				# jika anda mencoba untuk mendekripsi token yang sudah expired
				# anda akan mendapatkan error khusus, kita menangani error nya disini
        return jsonify({"result": "fail", "msg": "Your token has expired"})
    except jwt.exceptions.DecodeError:
				# jika ada permasalahan lain ketika proses decoding,
        # kita akan tangani di sini
        return jsonify(
            {"result": "fail", "msg": "There was an error while logging you in"}
        )

@app.route("/secret")
def secret():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        return render_template("secret.html")
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))

@app.route("/sign_up/save", methods=["POST"])
def sign_up():
    username_receive = request.form["username_give"]
    password_receive = request.form["password_give"]
    password_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()
    doc = {
        "username": username_receive,  # id
        "password": password_hash,  # password
        "profile_name": username_receive,  # user's name is set to their id by default
        "profile_pic": "",  # profile image file name
        "profile_pic_real": "profile_pics/profile_placeholder.png",  # a default profile image
        "profile_info": "",  # a profile description
    }
    db.akun.insert_one(doc)
    return jsonify({"result": "success"})

@app.route("/sign_up/check_dup", methods=["POST"])
def check_dup():
    # ID we should check whether or not the id is already taken
    username_receive = request.form["username_give"]
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({"result": "success", "exists": exists})

@app.route("/input")
def input_warga():
    return render_template('input.html')

@app.route("/input/tambah")
def tambah():
      token_receive = request.cookies.get("mytoken")
      payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
      user_info = db.akun.find_one({"username": payload["id"]})
      ket_rw = user_info['username'][-1]
      return render_template('tambah_kk.html', rw = ket_rw)

@app.route("/api/kk", methods=["POST"])
def tambah_kk():
    nama_receive = request.form['nama_give'],
    noKK_receive = request.form['nomorKK_give']
    rw_receive = request.form['rw_give']
    rt_receive = request.form['rt_give']
    doc = {
        'kepala': nama_receive,
        'nomorKK': noKK_receive,
        'rw' : rw_receive,
        'rt' : rt_receive,
    }
    db.kartu_keluarga.insert_one(doc)
    return jsonify({'msg':'Berhasil Ditambahkan'})

@app.route("/api/kk", methods=["GET"])
def kk_get():
    kk_list = list(db.kartu_keluarga.find({}, {'_id': False}))
    return jsonify({'kartu_keluarga': kk_list})

@app.route('/tambah-anggota/<keyword>')
def tambah_anggota(keyword):
    pisah = keyword.split('-')
    noKK = pisah[-1]
    kepala = pisah[0]
    
    return render_template(
        'input_anggota.html',
        nokk = noKK,
        kepala = kepala
    )

@app.route('/edit-anggota/<keyword>', methods=["GET"])
def edit_anggota(keyword):
    pisah = keyword.split('-')
    nik = pisah[-1]
    nama = pisah[0]
    return render_template(
        'edit_anggota.html',
        nik = nik,
        nama = nama
    )

@app.route("/edit-anggota", methods=["POST"])
def anggota_edit():
    token_receive = request.cookies.get("mytoken")
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
    user_info = db.akun.find_one({"username": payload["id"]})
    ket_rw = user_info['username'][-1]
    nama_receive = request.form['nama_give']
    nik_receive = request.form['nik_give']
    ttl_receive = request.form['ttl_give']
    tLahir_receive = request.form['tLahir_give']
    jk_receive = request.form['jk_give']
    rt_receive = request.form['rt_give']
    agama_receive = request.form['agama_give']
    pendidikan_receive = request.form['pendidikan_give']
    jenisPekerjaan_receive = request.form['jenisPekerjaan_give']
    golDarah_receive = request.form['golDarah_give']

    doc = {
          'nama' : nama_receive,
          'nik' : nik_receive,
          'tgl_lahir' : ttl_receive,
          'tmpt_lahir' : tLahir_receive,
          'jk' : jk_receive,
          'rw' : ket_rw,
          'rt': rt_receive,
          'agama' : agama_receive,
          'pendidikan' : pendidikan_receive,
          'pekerjaan' : jenisPekerjaan_receive,
          'golDarah' : golDarah_receive
    }
    db.warga.update_one(
        {'nik': nik_receive},
        {'$set': doc}
    )
    return jsonify({'msg':'Data Disimpan!'})

@app.route('/input/data-lengkap', methods=["GET"])
def data_lengkap():
    token_receive = request.cookies.get("mytoken")
    payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
    user_info = db.akun.find_one({"username": payload["id"]})
    ket_rw = user_info['username'][-1]
    print(ket_rw)
    return render_template(
        'data_lengkap.html', rw = ket_rw
    )

@app.route('/daftar', methods=["POST"])
def daftar():
    code_receive = request.form['code_give']
    wilayah_receive = request.form['wilayah_give']
    nick_receive = request.form['nick_give']
    pass_receive = request.form['pass_give']
    username_receive = request.form['username_give']
    doc = {
          "code" : code_receive,
          "wilayah" : wilayah_receive,
          "nick" : nick_receive,
          "pass" : hashlib.sha256(pass_receive.encode("utf-8")).hexdigest(),
          "username" : username_receive,
    }
    db.akun.insert_one(doc)
    return jsonify({'msg':"Berhasil"})

@app.route('/daftar', methods=["GET"])
def daftar_GET():
        return render_template('daftar.html')

@app.route('/delete/akun', methods=['POST'])
def delete_akun():
    nik_receive = request.form['nik_give']
    db.warga.delete_one({'nik' : nik_receive})
    return jsonify({'msg' : "Akun Berhasil Di Hapus"})

@app.route('/delete/kk', methods=['POST'])
def delete_kk():
    noKK_receive = request.form['noKK_give']
    db.kartu_keluarga.delete_one({'nomorKK' : noKK_receive})
    db.warga.delete_many({'noKK' : noKK_receive})
    return jsonify({'msg' : "Akun Berhasil Di Hapus"})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)