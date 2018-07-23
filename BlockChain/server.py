from flask import Flask, jsonify, request
import flask
import json
from textwrap import dedent
from uuid import uuid4

from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-','')

blockchain = Blockchain()

@app.route('/mine', method=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    
    proof = blockchain.proof_of_work(last_proof)
    
    blockchain.new_transaction(
    sender='0',
    recipient=node_identifier,
    amount=1
    
    )
    
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    
    response = {
        'message':'new block forged',
        'index': block['index'],
        'transactions':block['transactions'],
        'proof':block['proof'],
        'previous_hash':block['previous_hash']
    }
    return jsonify(response), 200
    
@app.route('/transactions/new', method=['POST'])
def new_transaction():
    values = request.get_json()
    
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'missing values', 400
    
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    
    response = {'message':'Transaction will be added to Block{0}'.format(index)}
    
    return jsonify(response), 201

@app.route('/chain', method = ['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    
    return flask.jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
