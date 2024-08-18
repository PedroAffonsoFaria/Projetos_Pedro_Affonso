#!/usr/bin/env python
# coding: utf-8

# # **Mario Project**

# O intuito desse projeto é aprender um pouco mais sobre o conteúdo de Reinforcement Learning aplicando algo que sempre tive contato, como o mundo dos jogos, a ideia veio do Nicholas Renotte.

# Para executarmos esse projeto devemos:
# 1º - Configurar um ambiente Mario
# 2º - Pré-Processá-lo o jogo para para uma IA Aplicada
# 3º - Treinar o modelo para jogar Mario (Reinforcement Learning)
# 4º - Testar para gerar os Resultados Finais 

# **1º - Configurar um ambiente Mario**

# Para configurarmos um ambiente de jogo utilizaremos o "Gym" que é uma estrutura comum que torna mais fácil treinar IA para jogar e interagir com outros ambientes simulados. Para nosso projeto vamos utilizar: gym-super-mario-bros 7.3.2, que foi construido em cima do Emulador NES (nes-py 8.1.8) do Pyhton
# 

# In[7]:


#Instalar estrutura Gym-super-mario-bros e Emulador Nes-py (é necessário ter o Microsoft Visual C++)
get_ipython().system('pip install gym_super_mario_bros==7.3.0 nes_py')


# In[8]:


# Importar o jogo
import gym_super_mario_bros

#Importando a nova versão do gym
import gymnasium as gym

#Importar o Controle/Joypad wrapper
from nes_py.wrappers import JoypadSpace

#Importar os Controles SIMPLIFICADOS
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT


# Dica: Tente sempre simplificar o ambiente do jogo o máximo possível, porque quanto mais complexo for, mais difícil vai ser para a IA para aprender a jogar o jogo

# In[ ]:


# Ações que nossa IA vai ser capaz de realizar (Controles)
SIMPLE_MOVEMENT


# In[9]:


#Setar o jogo
env = gym_super_mario_bros.make('SuperMarioBros-v0',apply_api_compatibility=True,render_mode="human" )

# Nós embrulhamos as combinações para simplificarmos como a IA vai aprender 
env = JoypadSpace(env,SIMPLE_MOVEMENT)


# In[ ]:


#Número de combinações de botões diferentes que você pode realmente usar o jogo
env.action_space


# Dicas: observation_space (o que você realmente receberá de seu ambiente)

# In[ ]:


#Quadro do jogo (240 pixels x 256 pixels x 3)
env.observation_space.shape


# In[ ]:


# Podemos realizar moviementos aleatórios dentro do jogo
SIMPLE_MOVEMENT[env.action_space.sample()]


# In[ ]:


# Criamos o sinalizador - verificar se reiniciamos o jogo ou não
done = True
# Loop por cada quadro do jogo
for step in range(100000):
    if done:
        # Iniciar o jogo
        env.reset()
        #'env.step' faz com que passamos por uma ação dentro do jogo
        # Realizando ações aleatórias (env.action_space.sample())
    state,reward,done,info,_ = env.step(env.action_space.sample())
    # Mostrar o jogo na tela
    env.render()
    #Fechar o jogo
env.close()


# **Resultados Primeira Simulação**: O Mario fica pulando repetidas vezes no segundo cano, mas não consegue ultrapassar, pois nossa IA, ainda não está aprendendo. Ele consegue passar do primeiro cano, pois estão sendo realizadas ações aleatórias, que permitiu com que ele conseguisse passar.

# In[ ]:


env.close()


# In[ ]:


#o estado neste caso é o quadro do jogo
state = env.reset()


# In[ ]:


#240 pixels de altura, 256 de largura e 3 canais (logo é uma imagem colorida)
array = state[0]
print(array.shape)


# In[ ]:


#Primeiro passo ('state')
env.step(1)[0]


# In[ ]:


# Segundo Passo ('reward')
# Explicando melhor o reward: The reward function assumes the objective of the game is to move as far right as possible (increase the agent's x value), as fast as possible, without dying. To model this game, three separate variables compose the reward:(fonte:https://pypi.org/project/gym-super-mario-bros/)
# Nossa tarefa é fazer com que a IA maximize essa IA
env.step(1)[1]


# In[ ]:


# Terceiro Passo ('done')
# Verificamos se morremos ou não, ou se o jogo acabou ou não
env.step(1)[2]


# In[ ]:


# Quarto passo
env.step(1)[3]


# In[ ]:


# Quinto passo ('info')
# Informações: numero de moedas coletadas, bandeiras coletadas, vidas, etc..
env.step(1)[4]


# **2º - Pré-processamento do Jogo**

# Precisamos pré-processar nossos dados do jogo antes de tornarmos em uma IA. Nós vamos ter duas etapas principais de pré-processamento: 1º escala de cinza; 2º empilhamento de quadros 

# 1º - Escala de Cinza: Uma imagem colorida tem 3x mais pixels para processar, ao convertermos para escala de cinza reduz os dados que ele deve aprender, logo: aprendizado mais rápido = IA mais rápida :)

# 2º - Empilhamento de quadros: O empilhamento de quadros permite que nossa IA tenha um contexto, ao empilharmos quadros consecutivos, estamos dando memória ao nosso modelo (e ajuda determinar trajetória e velocidade) e verá os movimentos do Mario e de seus inimigos!

# In[10]:


#Instalando o Pytorch
get_ipython().system('pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118')


# In[11]:


get_ipython().system('pip install stable-baselines3[extra]')


# **Escala de Cinza** - Utilizaremos para conseguirmos converter o jogo colorido em uma versão em escala de cinza, reduzindo a quantidade de informações que nosso modelo de IA deve produzir, o 'GrayScaleObservation'
# 

# **Empilhamentos de Quadros** - Para permitirmos capturar alguns quadros enquanto estamos jogando Mario e nosso modelo vai saber o que aconteceu nos quadros anteriores, utilizamos o 'FrameStack'

# E para conseguirmos implementar nosso modelo de Reinforcement Learning, precisaremos vetorizá-lo para podermos usá-lo sem IA. Para isso utilizamos de Wrappers que vetorizam. E a principal biblioteca para Reinforcement Learning que vamos utilizar é a 'stable_baselines3'. Utilizaremos o 'DummyVecEnv' que envolve nosso ambiente base dentro de um wrapper de vetorização 

# In[12]:


#Importando Frame Stacker e GrayScalling Wrapper
from gym.wrappers import GrayScaleObservation
#Importando Wrappers de Vetorização
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
#Mostrar o impacto de empilhamento de quadros
from matplotlib import pyplot as plt


# In[13]:


import gym
import numpy as np

# 1ª etapa de pré-processamento: Criar o ambiente base
def make_env():
    env = gym_super_mario_bros.make('SuperMarioBros-v0', apply_api_compatibility=True, render_mode="human")
    # 2ª etapa de pré-processamento: Simplificar os controles
    env = JoypadSpace(env, SIMPLE_MOVEMENT)
    # 3ª etapa de pré-processamento: Escala de Cinza
    env = GrayScaleObservation(env, keep_dim=True)
    return env

# Customização do DummyVecEnv para remover o argumento `seed`
class CustomEnvWrapper(gym.Env):
    def __init__(self, env):
        super(CustomEnvWrapper, self).__init__()
        self.env = env
        self.observation_space = env.observation_space
        self.action_space = env.action_space
    #Criamos a função reset, pois quando utilizamos a função 'env.step', não estava rodando por causa da seed, então excuímos os argumentos extras 
    def reset(self):
        obs = self.env.reset()  
        if isinstance(obs, tuple):  # Se for uma tupla, pegamos o primeiro elemento
            obs = obs[0]
        return np.array(obs, dtype=np.float32)  # Garantir que a saída seja um array numpy
    # A função step, definimos com 5 argumentos, pois quando utilizamos a função com 'done' ao invés de 'terminated,truncated', o número de argumentos não estava sendo o suficiente
    def step(self, action):
        obs, reward, terminated,truncated, info = self.env.step(action)
        if isinstance(obs, tuple):  # Se for uma tupla, pegamos o primeiro elemento
            obs = obs[0]
        return np.array(obs, dtype=np.float32), reward, terminated, info  # Garantir que a saída seja um array numpy

    def render(self, mode='human'):
        return self.env.render(mode)

    def close(self):
        self.env.close()

# Cria o ambiente
wrapped_env = CustomEnvWrapper(make_env())

# 4ª etapa de pré-processamento: Wrap dentro do Dummy Environment
env = DummyVecEnv([lambda: wrapped_env])
#5ª etapa de pré-processamento: Empilhar os quadros
env = VecFrameStack(env,4,channels_order='last')


# In[14]:


state = env.reset()


# In[15]:


state.shape


# In[16]:


action = env.action_space.sample()


# In[17]:


state, reward, done, info = env.step([5])


# Diferença de pixels quando utilizamos escalas de cinza

# In[ ]:


#Números de pixels quando utilizamos escala de cinza
240*256*1


# In[ ]:


#Números de pixels quando NÃO utilizamos escala de cinza
240*256*3


# In[82]:


# Verificando o quadro do jogo utilizando matplotlib
plt.imshow(state[0])


# In[18]:


#Representação de cada um dos Quadro Empilhados
plt.figure(figsize=(20,16))
for idx in range(state.shape[3]):
    plt.subplot(1,4,idx+1)
    plt.imshow(state[0][:,:,idx])
plt.show()


# **Conclusão**:Nesse quadro podemos ver que o Mario está subindo, pois utilizamos o passo "5" no "simple movement", e nesse caso permitimos que empilhassemos cada um desses quadros. Agora você pode ver que nosso modelo IA terá algum tipo de memória e conseguiremos ver a velocidade/movimento que está sendo realizado 

# # Reinforcement Learning

# Nossos 4 passos principais vão ser: **Agente, Recompensa, Ambiente, Ação**

# No nosso caso atual: O Mario é nosso **Agente**, e ele pode realizar **Ações**, como: pular, mover para direita.No nosso cenário do jogo que será o **Ambiente** que iremos trabalhar. E dependendo do resultado da sua ação ele pode ter uma **Recompensa** ou uma Penalidade. A IA que controla o Mario aprende quais ações tomar dentro do ambiente para maximizar essa recompensa.
#         

# **3º - Treinar o modelo**

# O algoritmo de Reinforcement Learning que iremos utilizar se chama **PPO (Otimização de política proximal)**

# In[19]:


# Importar 'os' para gerenciamento de onde queremos salvar os modelos 
import os
# Importar PPO para os algoritmos
from stable_baselines3 import PPO
# Import Base Callback para salvar os modelos
from stable_baselines3.common.callbacks import BaseCallback


# In[20]:


# Definindo para ter algum lugar para salvar o modelo a cada x números de etapas
class TrainAndLoggindCallback(BaseCallback):
    
    def __init__(self,check_freq,save_path,verbose=1):
        super(TrainAndLoggindCallback, self).__init__(verbose)
        self.check_freq = check_freq
        self.save_path = save_path
        
    def _init_callback(self):
        if self.save_path is not None:
            os.makedirs(self.save_path,exist_ok=True)
            
    def _on_step(self):
        if self.n_calls % self.check_freq == 0:
            model_path = os.path.join(self.save_path, 'best_model_{}'.format(self.n_calls))
            self.model.save(model_path)
            
        return True


# In[22]:


CHECKPOINT_DIR = 'C:/Users/ADM/OneDrive/Documentos/Projetos de Machine Learning/Projeto Mario/train'
LOG_DIR = 'C:/Users/ADM/OneDrive/Documentos/Projetos de Machine Learning/Projeto Mario/logs'


# In[23]:


# Salvando o retorno da chamada 
callback = TrainAndLoggindCallback(check_freq=10000, save_path=CHECKPOINT_DIR)


# In[24]:


#Criando o modelo de IA
#CnnPolicy estamos utilizando um tipo específico de rede neural que é rápido para processamento de imagens
model = PPO('CnnPolicy', env,verbose=1,tensorboard_log=LOG_DIR,learning_rate=0.000001,
           n_steps=512)


# In[ ]:


# Treinando o modelo de IA, essa é a parte que o modelo começa a aprender
model.learn(total_timesteps=1000000,callback=callback)


# In[ ]:





# In[ ]:




